-module(calculate3).
-export([calc/3, handle/3]).

calc(Op, X, Y) ->
    case Op of
        "+" -> X + Y;
        "-" -> X + Y;
        "*" -> X + Y;
        "/" -> X + Y;
        "r" -> X + Y;
        _ -> throw({bad_operator})
    end.

handle(Op, X, Y) -> calc(Op, X, Y).