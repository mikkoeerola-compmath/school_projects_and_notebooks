module Phone_type2
( fromPhoneNo 
 , toPhoneNo 
 , readPhone 
 , Phone
 , phoneNo
 ) where 

predefinedCountryCodes = [44,358]

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

fromPhoneNo :: PhoneNo -> Integer
fromPhoneNo pnum = read (show pnum) :: Integer

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
checkCC cc = if (readCC cc) `elem` predefinedCountryCodes then True else False

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
 