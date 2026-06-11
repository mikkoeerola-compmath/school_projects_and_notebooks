module Phone_book
( addEntry
, findEntries
) where

import Phone_type2 as Pt

data PhoneBookEntry = PhoneBookEntry { name :: String , phone :: Phone } deriving(Eq, Ord, Show)
type PhoneBook = [PhoneBookEntry]

findEntries :: String -> PhoneBook -> PhoneBook
findEntries ss pBook = filter (\pBookIn -> name pBookIn == ss) pBook

addEntry :: String -> String -> String -> String -> PhoneBook -> PhoneBook
addEntry ss pty cc pno pBook
 | (filter (\pb -> ((name pb) == ss) && (Pt.phoneNo (phone pb) == Pt.toPhoneNo (read pno :: Integer))) pBook) /= [] = pBook
 | otherwise = (PhoneBookEntry {name = ss, phone = readPhone pty cc pno}):pBook
