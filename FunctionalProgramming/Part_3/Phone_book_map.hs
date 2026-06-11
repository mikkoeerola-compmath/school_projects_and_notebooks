module Phone_book_map
( addEntry
, findEntries
, Phonebook
) where

import Phone_type2 as Pt
import qualified Data.Map as Map

type Name = String
type Phonebook = Map.Map Name [Phone]

ridOfMaybe :: Maybe [Phone] -> [Phone]
ridOfMaybe (Just a) = a
ridOfMaybe Nothing = []

findEntries :: Name -> Phonebook -> [Phone]
findEntries ss pBook = ridOfMaybe (Map.lookup ss pBook)

addEntry :: Name -> String -> String -> String -> Phonebook -> Phonebook
addEntry ss pty cc pno pBook
 | findEntries ss pBook == [] = Map.insert ss [Pt.readPhone pty cc pno] pBook
 | toPhoneNo (read pno :: Integer) `elem` map phoneNo (findEntries ss pBook) = pBook
 | otherwise = Map.insertWith (\phone ys -> phone ++ ys) ss [Pt.readPhone pty cc pno] pBook