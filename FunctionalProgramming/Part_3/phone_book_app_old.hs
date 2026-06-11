import System.Environment
import qualified Data.List as Ls
import System.IO
import Phone_type2
import System.Directory

matchFunction :: [(String, [String] -> IO ())]
matchFunction = [ ("add", addEntry)
                , ("find", findEntries)
                ]

main = do
    putStrLn "Welcome to phone book application"
    writeFile "phonebook.txt" ""
    loopReadLine

loopReadLine :: IO ()
loopReadLine = do
    line <- getLine
    let command = head $ words line
        args = tail $ words line
    if command == "quit"
        then do 
            putStrLn "bye"
        else do
            if not (command == "add" || command == "find")
                then putStrLn "Cannot do that"
                else 
                    let (Just action) = lookup command matchFunction
                    in action args
            loopReadLine

addEntry :: [String] -> IO ()
addEntry (name:stList) = do 
                let pNum = readPhone (stList!!0) (stList!!1) (stList!!2)
                handle <- openFile "phonebook.txt" ReadMode
                contents <- hGetContents handle
                isEntered <- findEntries' contents name (show (phoneNo pNum))
                if isEntered
                    then return ()
                    else do
                        hClose handle
                        appendFile "phonebook.txt" (name ++ " " ++ (show pNum) ++ "\n")
                putStrLn "Done"

findEntries :: [String] -> IO ()
findEntries [name] = do
                    contents <- readFile "phonebook.txt"
                    let pNumList = lines contents
                        pNumLines = map (dropWhile (/= '+')) [result | result <- pNumList, name `Ls.isPrefixOf` result]
                        pNumLines' = reverse (Ls.intersperse "," pNumLines)
                        pNum = (Ls.concat pNumLines')
                    putStrLn ("[" ++ pNum ++ "]")

findEntries' :: String -> String -> String -> IO Bool
findEntries' contents name pNum = do
                    let isName = name `Ls.isInfixOf` contents
                        ispNum = pNum `Ls.isInfixOf` contents
                    return (isName && ispNum)

