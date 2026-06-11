data PhoneType = WorkLandline | PrivateMobile | WorkMobile | Other deriving (Show, Read, Eq, Ord)

data CountryCode = CountryCode Integer deriving(Eq, Ord)

data PhoneNo = PhoneNo Integer deriving(Eq, Ord)

instance Show CountryCode where
  show (CountryCode i) = "+" ++ show i

instance Num CountryCode where
  fromInteger i = toCountryCode i
  (+) (CountryCode i) (CountryCode j) = CountryCode (i + j)
  (-) (CountryCode i) (CountryCode j) = CountryCode (i - j)
  (*) (CountryCode i) (CountryCode j) = CountryCode (i * j)

instance Show PhoneNo where
  show (PhoneNo i) = show i

instance Num PhoneNo where
  fromInteger i = toPhoneNo i
  (+) (PhoneNo i) (PhoneNo j) = PhoneNo (i + j)
  (-) (PhoneNo i) (PhoneNo j) = PhoneNo (i - j)
  (*) (PhoneNo i) (PhoneNo j) = PhoneNo (i * j)

toCountryCode :: Integer -> CountryCode
toCountryCode x = if x < 0 then error "Negative country code" else CountryCode x

toPhoneNo :: Integer -> PhoneNo
toPhoneNo x = if x < 0 then error "Negative phone number" else PhoneNo x

data Phone = Phone { phoneType :: PhoneType
               , countryCode :: CountryCode
               , phoneNo :: PhoneNo
             } deriving(Eq, Ord)

instance Show Phone where
  show (Phone pt cc pnum) = show cc ++ " " ++ show pnum ++ " (" ++ show pt ++ ")"

makePhone :: PhoneType -> CountryCode -> PhoneNo -> Phone
makePhone pt cc pnum
 | cc < 0 = error "Negative country code"
 | pnum < 0 = error "Negative phone number"
 | otherwise = Phone pt cc pnum

-- Task 2.3:

onlyDigits :: String -> Bool
onlyDigits "" = True
onlyDigits (x:xs) = (elem x j) && onlyDigits xs
  where j = ['0'..'9']

readCC :: String -> Integer
readCC (x:y:xs)
 | x:y:[] == "00" = readCC xs
 | x == '+' = readCC (y:xs)
readCC xs
 | onlyDigits xs = read xs :: Integer
 | otherwise = error "Incorrect country code"

checkCC :: String -> Bool
checkCC cc = if readCC cc `elem` [358, 101, 123] then True else False

checkPT :: String -> Bool
checkPT st = if st `elem` map show [WorkLandline, PrivateMobile, WorkMobile, Other]
             then True else False

readPhone :: String -> String -> String -> Phone
readPhone "" _ _ = error "Missing phone type"
readPhone _ "" _ = error "Empty country code"
readPhone _ _ "" = error "Empty phone number"
readPhone pt cc pnum
 | not (checkCC cc) = error "Unknown country code"
 | not (checkPT pt) = error "Incorrect phone type"
 | not (onlyDigits pnum) = error "Incorrect phone number"
 | otherwise = Phone {phoneType = read pt :: PhoneType, countryCode = (toCountryCode (readCC cc)), phoneNo = toPhoneNo (read pnum :: Integer)}

data PhoneBookEntry = PhoneBookEntry { name :: String , phone :: Phone } deriving(Eq, Ord, Show)
type PhoneBook = [PhoneBookEntry]

findEntries :: String -> PhoneBook -> PhoneBook
findEntries ss pBook = filter (\pBookIn -> name pBookIn == ss) pBook

addEntry :: String -> String -> String -> String -> PhoneBook -> PhoneBook
addEntry ss pty cc pno pBook
 | (filter (\pb -> ((name pb) == ss) && (phoneNo (phone pb) == toPhoneNo (read pno :: Integer))) pBook) /= [] = pBook
 | otherwise = (PhoneBookEntry {name = ss, phone = readPhone pty cc pno}):pBook
