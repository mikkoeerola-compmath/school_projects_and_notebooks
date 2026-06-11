{-import Control.Concurrent
import System.IO

main = do
 input1 <- getLine
 input2 <- getLine
 input3 <- getLine
 input4 <- getLine
 mVal1 <- newEmptyMVar 
 mVal2 <- newEmptyMVar
 msg <- newEmptyMVar
-- parameters for start / guess are: name, value_in, value_out, message_to_other, int_list 
 forkIO (start (read input1::String) mVal1 mVal2 msg (read input2::[Int]))
 forkIO (guess (read input3::String) mVal2 mVal1 msg (read input4::[Int]))
 threadDelay 2000000 -- without this the main thread will die and so will the forked threads

-- won already when starting because the list is empty
start :: String -> MVar Int -> MVar Int -> MVar String -> [Int] -> IO ()
start myName mVal1 mVal2 msg [] = do
 putMVar msg "I won"
 putMVar mVal2 0 -- has to put a value because thats what the player is reading
 putStrLn (myName ++ " won")

-- starting is different from other situations
start myName mVal1 mVal2 msg (i:is) = do
 putStrLn (myName ++ " guesses " ++ (show i))
 putMVar mVal2 i
 putMVar msg "your turn"
 guess myName mVal1 mVal2 msg is

--Here starts my part

guess :: String -> MVar Int -> MVar Int -> MVar String -> [Int] -> IO ()
guess myName myIn myOut msg myList = do
    m <- takeMVar msg
    case m of
        "your turn" -> do
            v <- takeMVar myIn
            if v `elem` myList then do
                putStrLn (myName ++ " lost")
                putMVar msg "I lost"
                putMVar myOut 0
            else case myList of
                [] -> do
                    putStrLn (myName ++ " won")
                    putMVar msg "I won"
                    putMVar myOut 0
                (x:xs) -> do
                    putStrLn (myName ++ " guesses " ++ show x)
                    putMVar myOut x
                    putMVar msg "your turn"
                    guess myName myIn myOut msg xs
        "I won" -> do
            putStrLn (myName ++ " lost")
        "I lost" -> do
            putStrLn (myName ++ " won")-}
