data PhoneType = WorkLandline | PrivateMobile | WorkMobile | Other deriving (Show, Read, Eq, Ord)

data CountryCode = MakeCountryCode Integer deriving(Eq, Ord)

data PhoneNo = MakePhoneNo Integer deriving(Eq, Ord)

instance Show CountryCode where
  show (MakeCountryCode i) = "+" ++ show i

instance Num CountryCode where
  fromInteger i = toCountryCode i
  (+) (MakeCountryCode i) (MakeCountryCode j) = MakeCountryCode (i + j)
  (-) (MakeCountryCode i) (MakeCountryCode j) = MakeCountryCode (i - j)
  (*) (MakeCountryCode i) (MakeCountryCode j) = MakeCountryCode (i * j)

instance Show PhoneNo where
  show (MakePhoneNo i) = show i

instance Num PhoneNo where
  fromInteger i = toPhoneNo i
  (+) (MakePhoneNo i) (MakePhoneNo j) = MakePhoneNo (i + j)
  (-) (MakePhoneNo i) (MakePhoneNo j) = MakePhoneNo (i - j)
  (*) (MakePhoneNo i) (MakePhoneNo j) = MakePhoneNo (i * j)

toCountryCode :: Integer -> CountryCode
toCountryCode x = if x < 0 then error "Negative country code" else MakeCountryCode x

toPhoneNo :: Integer -> PhoneNo
toPhoneNo x = if x < 0 then error "Negative phone number" else MakePhoneNo x

fromPhoneNo :: PhoneNo -> Integer
fromPhoneNo pnum = read (show pnum)

readPhoneType :: String -> Maybe PhoneType
readPhoneType ss = if ss == "" then Nothing else Just (read ss :: PhoneType)

readCountryCode :: String -> Maybe CountryCode
readCountryCode ss = if ss == "" then Nothing else Just (toCountryCode (read ss :: Integer))

readPhoneNo :: String -> PhoneNo
readPhoneNo ss = toPhoneNo (read ss :: Integer)

data Phone = Phone { phoneType :: Maybe PhoneType
               , countryCode :: Maybe CountryCode
               , phoneNo :: PhoneNo
             } deriving(Eq, Ord)

instance Show Phone where
  show (Phone Nothing Nothing pnum) = show pnum
  show (Phone Nothing (Just cc) pnum) = show cc ++ " " ++ show pnum
  show (Phone (Just pt) Nothing pnum) = show pnum ++ " (" ++ show pt ++ ")"
  show (Phone (Just pt) (Just cc) pnum) = show cc ++ " " ++ show pnum ++ " (" ++ show pt ++ ")"

makePhone :: PhoneType -> CountryCode -> PhoneNo -> Phone 
makePhone pt cc pnum
 | cc < 0 = error "Negative country code"
 | pnum < 0 = error "Negative phone number"
makePhone pt cc pnum = Phone (Just pt) (Just cc) pnum

readPhone :: String -> String -> String -> Phone
readPhone _ _ "" = error "Empty phone number"
readPhone pt cc pnum = Phone {phoneType = readPhoneType pt , countryCode = readCountryCode cc, phoneNo = readPhoneNo pnum}
