data PhoneType = WorkLandline | PrivateMobile | WorkMobile | Other deriving (Show, Read, Eq)

type CountryCode = Int
type PhoneNo = Int

data Phone = Phone { phoneType :: PhoneType
               , countryCode :: CountryCode
               , phoneNo :: PhoneNo
             } deriving(Eq, Read, Show)

 {-instance Show Phone where
  show (Phone _ 0 _) = "Negative country code"
  show (Phone _ _ 0) = "Negative phone number"
  show (Phone pt cc pnum) = "Phone (" ++ show pt ++ ", " ++ show cc ++ ", " ++ show pnum ++ ")"
-}
makePhone :: PhoneType -> CountryCode -> PhoneNo -> Phone
makePhone pt cc pnum
 | cc < 0 = error "Negative country code"
 | pnum < 0 = error "Negative phone number"
 | otherwise = Phone pt cc pnum
