import Data.List as Ls

data Month = MakeMonth Integer deriving (Eq, Ord)

instance Show Month where
    show month
      | fromMonth month < 10 = "0" ++ (show $ fromMonth month)
      | otherwise = show $ fromMonth month

toMonth :: Integer -> Month
toMonth x
 | x < 1 = error "Minimum month number is 1"
 | x > 12 = error "Maximum month number is 12"
 | otherwise = MakeMonth x

fromMonth :: Month -> Integer
fromMonth (MakeMonth i) = i

data Day = MakeDay Integer deriving (Eq, Ord)

instance Show Day where
    show day
      | fromDay day < 10 = "0" ++ (show $ fromDay day)
      | otherwise = show $ fromDay day

toDay :: Integer -> Day
toDay x
 | x < 1 = error "Minimum day number is 1"
 | x > 31 = error "Maximum day number is 31"
 | otherwise = MakeDay x

fromDay :: Day -> Integer
fromDay (MakeDay i) = i

data Year = MakeYear Integer deriving (Eq, Ord)

instance Show Year where
    show year = show $ fromYear year

toYear :: Integer -> Year
toYear x
 | x == 0 = error "No year 0"
 | otherwise = MakeYear x

fromYear :: Year -> Integer
fromYear (MakeYear i) = i

data Date = Date { year :: Year, month :: Month, day :: Day } deriving (Eq, Ord)

instance Show Date where
    show date = (show $ year date) ++ "-" ++ (show $ month date) ++ "-" ++ (show $ day date)

correctDate :: Integer -> Integer -> Integer -> Bool
correctDate 0 _ _ = False
correctDate y m d
 | (elem m [1,3,5,7,8,10,12]) && (elem d [1..31]) = True
 | (elem m [4,6,9,11]) && (elem d [1..30]) = True
 | (m==2) && (elem d [1..28]) = True
 | (leapYear (toYear y)) && (m==2) && (d==29) = True
 | otherwise = False

makeDate :: Integer -> Integer -> Integer -> Date
makeDate y m d
 | correctDate y m d = Date { year = toYear y, month = toMonth m, day = toDay d }
 | otherwise = Date {year = toYear 1, month = toMonth 1, day = toDay 1 }

leapYear (MakeYear y)
 | mod y 400 == 0 = True
 | mod y 100 == 0 = False
 | mod y 4 == 0 = True
 | otherwise = False
{-
data EventInfo = EventInfo { name :: String
                           , place :: String
                           , date :: Date
                           } deriving(Eq)
 -}
printListOfCommands ::  IO ()
printListOfCommands = do
  putStrLn "I do not understand that. I understand the following:"
  putStrLn "*Event <name> happens at <place> on <date>"
  putStrLn "*Tell me about <eventname>"
  putStrLn "*What happens on <date>"
  putStrLn "*What happens at <place>"
  putStrLn "*Quit"

asListOfCommands :: [(String, [String] -> [EventInfo] -> IO [EventInfo])]
asListOfCommands = [("Event happens at on", addEvent),
                    ("Tell me about", tellEvent)
                    , ("What happens on", whatDate)
                    , ("What happens at", whatPlace)
                    ]

addEvent :: [String] -> [EventInfo] -> IO [EventInfo]
addEvent args events = do
    let newdate = makeDateList $ pickNums (last args)
        newname = (pickName args) \\ ['\'', '\'']
        newplace = pickName $ tail (args Ls.\\ (Ls.takeWhile (\x -> last x /= '\'') args))
        newplace' = newplace Ls.\\ ['\'', '\'']
        newEvent = EventInfo { name = newname, place = newplace', date = newdate}
    if year newdate == toYear 1 then do
        putStrLn "Bad date"
        return events
    else do
        let newEventList = checkAndAddEvent events newEvent
        putStrLn "ok"
        return newEventList

checkAndAddEvent :: [EventInfo] -> EventInfo -> [EventInfo]
checkAndAddEvent events newEvent
  | filter (\oldEvent -> (name oldEvent == name newEvent)) events /= []
    = newEvent:(Ls.deleteBy (\new old -> name new == name old) newEvent events)
  | otherwise = newEvent:events

pickNums :: String -> [Integer]
pickNums date = 
   let justNums = date Ls.\\ ['\'', '\'', '-', '-']
       checkNums = onlyDigits justNums
       y = take 4 justNums
       m = take 2 $ drop 4 justNums
       d = take 2 $ drop 6 justNums
    in if checkNums then [read y :: Integer, read m :: Integer, read d :: Integer]
       else [0,0,0]

makeDateList :: [Integer] -> Date
makeDateList [] = makeDate 0 0 0
makeDateList (x:y:z:xs) = makeDate x y z

pickName :: [String] -> String
pickName [] = ""
pickName [x] = x
pickName (x:y:xs)
  | not ("'" `Ls.isSuffixOf` x) = pickName ((x++" "++y):xs)
  | otherwise = x

tellEvent :: [String] -> [EventInfo] -> IO [EventInfo]
tellEvent args xs = do
    let nameAsOne = Ls.intercalate " " args
        eventName = Ls.delete '\'' $ Ls.delete '\'' nameAsOne
        eventMaybe = find (\x -> name x == eventName) xs
    if eventMaybe == Nothing then do
        putStrLn "I do not know of such event"
        return xs
    else do
        let Just event = eventMaybe
            text = "Event " ++ name event ++ " happens at " ++ place event ++ " on " ++ (show $ date event)
        putStrLn text
        return xs

whatDate :: [String] -> [EventInfo] -> IO [EventInfo]
whatDate args xs = do
    let eventDate = makeDateList $ pickNums (head args)
        events = filter (\x -> date x == eventDate) xs
    if events == [] then do
        putStrLn "Nothing that I know of"
        return xs
        else do
            let eventsSorted = Ls.sortBy (\x y -> compare (name x) (name y)) events
            printEventsOnDate eventsSorted
            return xs

printEventsOnDate :: [EventInfo] -> IO ()
printEventsOnDate [] = return () 
printEventsOnDate (x:xs) = do 
    let text = "Event " ++ name x ++ " happens on " ++ (show $ date x)
    putStrLn text
    printEventsOnDate xs

whatPlace :: [String] -> [EventInfo] -> IO [EventInfo]
whatPlace args xs = do
    let nameAsOne = Ls.intercalate " " args
        eventPlace = Ls.delete '\'' $ Ls.delete '\'' nameAsOne
        events = filter (\x -> place x == eventPlace) xs
    if events == [] then do
        putStrLn "Nothing that I know of"
        return xs
        else do
            let eventsSorted = Ls.sortBy (\x y -> compare (name x) (name y)) events
            printEventsAtPlace eventsSorted
            return xs

printEventsAtPlace :: [EventInfo] -> IO ()
printEventsAtPlace [] = return ()
printEventsAtPlace (x:xs) = do
    let text = "Event " ++ name x ++ " happens at " ++ place x
    putStrLn text
    printEventsAtPlace xs
{-
main = loop $ return []

loop :: IO [EventInfo] -> IO ()
loop ioEvents =
 do
 input <- getLine
 if input == "Quit"
   then putStrLn "bye"
   else doCommand input ioEvents
-}
doCommand :: String -> IO [EventInfo] -> IO ()
doCommand input ioEvents = do
  events <- ioEvents --Now you can use events as [EventInfo]
  let (args, commands) = handleCommands input
      actionMaybe = lookup (Ls.intercalate " " commands) asListOfCommands
  if checkCommand commands then do
      printListOfCommands
      loop $ return events
  else do
      let Just action = actionMaybe
      possiblyChangedEvents <- (action args events)
      loop $ return possiblyChangedEvents

handleCommands :: String -> ([String], [String])
handleCommands args =
   Ls.partition (\x -> ("'" `Ls.isPrefixOf` x || "'" `Ls.isSuffixOf` x)) (words args)

checkCommand :: [String] -> Bool
checkCommand comList =
  let com = intercalate " " comList
      commandList = map (\(x,y) -> x) asListOfCommands
  in not (com `elem` commandList)

onlyDigits :: String -> Bool
onlyDigits [] = True
onlyDigits (x:xt) = (x `elem` ['0'..'9']) && onlyDigits xt