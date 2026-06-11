module Phone_book_tree
( Phonebook(Empty)
 , addEntry
 , findEntries
 ) where

import Data.List
import Phone_type2
type Name = String
data Phonebook = Empty | Node String [Phone] Phonebook Phonebook deriving (Show,Eq)

makeTree :: Name -> String -> String -> String -> Phonebook
makeTree name pt cc pNr = Node name [readPhone pt cc pNr] Empty Empty

addEntry :: Name -> String -> String -> String -> Phonebook -> Phonebook
addEntry name pt cc pNr Empty = makeTree name pt cc pNr
addEntry name pt cc pNr (Node a st left right)
  | name == a && pNr `isInfixOf` (unwords (map show st)) = Node a st left right
  | name == a = Node a ((readPhone pt cc pNr):st)left right
  | name < a = Node a st (addEntry name pt cc pNr left) right
  | name > a = Node a st left (addEntry name pt cc pNr right)

findEntries :: Name -> Phonebook -> [Phone]
findEntries _ Empty = []
findEntries name (Node a st left right)
  | name == a = st
  | name < a = findEntries name left
  | name > a = findEntries name right
