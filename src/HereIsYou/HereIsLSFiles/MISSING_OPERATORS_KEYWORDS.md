# Missing Operators & Keywords for Python Parser Config

## Expanded Tracking Fields

This reference now includes hexadecimal support and a test-friendly metadata model.

Core fields:
- Ords (decimal code points per character)
- Binary (base-2 per character)
- Unicode (U+xxxx code points)
- Hexadecimal (0xXX per character)

Additional tracking fields for easier testing:
- Octal (0oXXX per character)
- UTF-8 bytes (0xXX per byte)
- Length in characters
- Length in bytes
- ASCII-only flag
- Whitespace flag
- Category key
- Deterministic test ID

The authoritative generator for all fields is now in:
- `pyparsingconfig.py` via `get_token_tracking_catalog()` and `build_tracking_test_vectors()`

## Tracking Row Template

| Token | Category | Test ID | Ords | Binary | Unicode | Hexadecimal | Octal | UTF-8 Bytes | Length Chars | Length Bytes | ASCII | Whitespace |
|---|---|---|---|---|---|---|---|---|---:|---:|---|---|
| `=` | assignment_operators | assignment_operators:001 | 61 | 111101 | U+003D | 0x3D | 0o075 | 0x3D | 1 | 1 | true | false |
| `yield from` | control_flow_keywords | control_flow_keywords:005 | 121, 105, 101, 108, 100, 32, 102, 114, 111, 109 | 1111001, 1101001, 1100101, 1101100, 1100100, 100000, 1100110, 1110010, 1101111, 1101101 | U+0079, U+0069, U+0065, U+006C, U+0064, U+0020, U+0066, U+0072, U+006F, U+006D | 0x79, 0x69, 0x65, 0x6C, 0x64, 0x20, 0x66, 0x72, 0x6F, 0x6D | 0o171, 0o151, 0o145, 0o154, 0o144, 0o040, 0o146, 0o162, 0o157, 0o155 | 0x79, 0x69, 0x65, 0x6C, 0x64, 0x20, 0x66, 0x72, 0x6F, 0x6D | 10 | 10 | true | true |

## Assignment Operators
Basic and augmented assignments that bind values to identifiers.

| Operator | Ords | Binary | Unicode | Description |
|----------|------|--------|---------|-------------|
| `=` | 61 | 111101 | U+003D | Basic assignment |
| `+=` | 43, 61 | 101011, 111101 | U+002B, U+003D | Add and assign |
| `-=` | 45, 61 | 101101, 111101 | U+002D, U+003D | Subtract and assign |
| `*=` | 42, 61 | 101010, 111101 | U+002A, U+003D | Multiply and assign |
| `/=` | 47, 61 | 101111, 111101 | U+002F, U+003D | Divide and assign |
| `//=` | 47, 47, 61 | 101111, 101111, 111101 | U+002F, U+002F, U+003D | Floor divide and assign |
| `%=` | 37, 61 | 100101, 111101 | U+0025, U+003D | Modulo and assign |
| `**=` | 42, 42, 61 | 101010, 101010, 111101 | U+002A, U+002A, U+003D | Exponent and assign |
| `&=` | 38, 61 | 100110, 111101 | U+0026, U+003D | Bitwise AND and assign |
| `\|=` | 124, 61 | 1111100, 111101 | U+007C, U+003D | Bitwise OR and assign |
| `^=` | 94, 61 | 1011110, 111101 | U+005E, U+003D | Bitwise XOR and assign |
| `>>=` | 62, 62, 61 | 111110, 111110, 111101 | U+003E, U+003E, U+003D | Right shift and assign |
| `<<=` | 60, 60, 61 | 111100, 111100, 111101 | U+003C, U+003C, U+003D | Left shift and assign |
| `:=` | 58, 61 | 111010, 111101 | U+003A, U+003D | Walrus operator (assignment expression) |

## Annotation Operators
Type hints and return type declarations.

| Operator | Ords | Binary | Unicode | Description |
|----------|------|--------|---------|-------------|
| `->` | 45, 62 | 101101, 111110 | U+002D, U+003E | Return type annotation |
| `:` | 58 | 111010 | U+003A | Parameter type annotation, dict separator, slice separator |

## Unpacking Operators
Context-dependent unpacking in assignments, function definitions, and calls.

| Operator | Ords | Binary | Unicode | Description |
|----------|------|--------|---------|-------------|
| `*` | 42 | 101010 | U+002A | Unpack iterable (different from multiply in context) |
| `**` | 42, 42 | 101010, 101010 | U+002A, U+002A | Unpack dictionary (different from exponent in context) |

## Structural/Separator Operators

| Operator | Ords | Binary | Unicode | Description |
|----------|------|--------|---------|-------------|
| `,` | 44 | 101100 | U+002C | Argument/element separator |
| `:` | 58 | 111010 | U+003A | Slice notation, dict key-value separator (also annotation) |
| `...` | 46, 46, 46 | 101110, 101110, 101110 | U+002E, U+002E, U+002E | Ellipsis (placeholder, continuation) |

## Scope Declaration Keywords
Keywords that affect variable scope.

| Keyword | Ords | Binary | Unicode | Description |
|---------|------|--------|---------|-------------|
| `global` | 103, 108, 111, 98, 97, 108 | 1100111, 1101100, 1101111, 1100010, 1100001, 1101100 | U+0067, U+006C, U+006F, U+0062, U+0061, U+006C | Declare global scope |
| `nonlocal` | 110, 111, 110, 108, 111, 99, 97, 108 | 1101110, 1101111, 1101110, 1101100, 1101111, 1100011, 1100001, 1101100 | U+006E, U+006F, U+006E, U+006C, U+006F, U+0063, U+0061, U+006C | Declare nonlocal scope |
| `lambda` | 108, 97, 109, 98, 100, 97 | 1101100, 1100001, 1101101, 1100010, 1100100, 1100001 | U+006C, U+0061, U+006D, U+0062, U+0064, U+0061 | Anonymous function (creates local scope) |
| `del` | 100, 101, 108 | 1100100, 1100101, 1101100 | U+0064, U+0065, U+006C | Delete/remove statement |
| `pass` | 112, 97, 115, 115 | 1110000, 1100001, 1110011, 1110011 | U+0070, U+0061, U+0073, U+0073 | No-operation (placeholder) |

## Control Flow Keywords
Keywords that control execution flow within scopes.

| Keyword | Ords | Binary | Unicode | Description |
|---------|------|--------|---------|-------------|
| `break` | 98, 114, 101, 97, 107 | 1100010, 1110010, 1100101, 1100001, 1101011 | U+0062, U+0072, U+0065, U+0061, U+006B | Exit loop |
| `continue` | 99, 111, 110, 116, 105, 110, 117, 101 | 1100011, 1101111, 1101110, 1110100, 1101001, 1101110, 1110101, 1100101 | U+0063, U+006F, U+006E, U+0074, U+0069, U+006E, U+0075, U+0065 | Skip iteration |
| `return` | 114, 101, 116, 117, 114, 110 | 1110010, 1100101, 1110100, 1110101, 1110010, 1101110 | U+0072, U+0065, U+0074, U+0075, U+0072, U+006E | Exit function/scope with value |
| `yield` | 121, 105, 101, 108, 100 | 1111001, 1101001, 1100101, 1101100, 1100100 | U+0079, U+0069, U+0065, U+006C, U+0064 | Generator yield value |
| `yield from` | 121, 105, 101, 108, 100, 32, 102, 114, 111, 109 | 1111001, 1101001, 1100101, 1101100, 1100100, 100000, 1100110, 1110010, 1101111, 1101101 | U+0079, U+0069, U+0065, U+006C, U+0064, U+0020, U+0066, U+0072, U+006F, U+006D | Delegate to sub-generator |
| `assert` | 97, 115, 115, 101, 114, 116 | 1100001, 1110011, 1110011, 1100101, 1110010, 1110100 | U+0061, U+0073, U+0073, U+0065, U+0072, U+0074 | Assertion/validation |
| `raise` | 114, 97, 105, 115, 101 | 1110010, 1100001, 1101001, 1110011, 1100101 | U+0072, U+0061, U+0069, U+0073, U+0065 | Raise exception |

## String Prefixes
Prefixes that modify string parsing behavior.

| Prefix | Ords | Binary | Unicode | Description |
|--------|------|--------|---------|-------------|
| `f` | 102 | 1100110 | U+0066 | f-string (formatted string literal) |
| `r` | 114 | 1110010 | U+0072 | Raw string (escape sequences ignored) |
| `b` | 98 | 1100010 | U+0062 | Bytes literal |
| `u` | 117 | 1110101 | U+0075 | Unicode (Python 2 legacy) |
| `fr` | 102, 114 | 1100110, 1110010 | U+0066, U+0072 | f-string raw combination |
| `rf` | 114, 102 | 1110010, 1100110 | U+0072, U+0066 | f-string raw combination (alternate order) |
| `br` | 98, 114 | 1100010, 1110010 | U+0062, U+0072 | Bytes raw combination |
| `rb` | 114, 98 | 1110010, 1100010 | U+0072, U+0062 | Bytes raw combination (alternate order) |

## Context Manager Keywords
Keywords related to context management.

| Keyword | Ords | Binary | Unicode | Description |
|---------|------|--------|---------|-------------|
| `with` | 119, 105, 116, 104 | 1110111, 1101001, 1110100, 1101000 | U+0077, U+0069, U+0074, U+0068 | Enter context manager |
| `as` | 97, 115 | 1100001, 1110011 | U+0061, U+0073 | Bind context variable (also used in except) |

## Exception Handling Keywords
Keywords for exception handling (partially covered).

| Keyword | Ords | Binary | Unicode | Description |
|---------|------|--------|---------|-------------|
| `try` | 116, 114, 121 | 1110100, 1110010, 1111001 | U+0074, U+0072, U+0079 | Start try block |
| `except` | 101, 120, 99, 101, 112, 116 | 1100101, 1111000, 1100011, 1100101, 1110000, 1110100 | U+0065, U+0078, U+0063, U+0065, U+0070, U+0074 | Catch exception |
| `else` | 101, 108, 115, 101 | 1100101, 1101100, 1110011, 1100101 | U+0065, U+006C, U+0073, U+0065 | Else clause (try-except) |
| `finally` | 102, 105, 110, 97, 108, 108, 121 | 1100110, 1101001, 1101110, 1100001, 1101100, 1101100, 1111001 | U+0066, U+0069, U+006E, U+0061, U+006C, U+006C, U+0079 | Finally clause |
| `raise` | 114, 97, 105, 115, 101 | 1110010, 1100001, 1101001, 1110011, 1100101 | U+0072, U+0061, U+0069, U+0073, U+0065 | Raise exception (also in control flow) |
| `as` | 97, 115 | 1100001, 1110011 | U+0061, U+0073 | Bind exception to variable (in except clause) |

## Comprehension Keywords
Keywords that create local scopes in comprehensions.

| Keyword | Ords | Binary | Unicode | Description |
|---------|------|--------|---------|-------------|
| `for` | 102, 111, 114 | 1100110, 1101111, 1110010 | U+0066, U+006F, U+0072 | Comprehension loop (already have) |
| `in` | 105, 110 | 1101001, 1101110 | U+0069, U+006E | Comprehension membership (already have) |
| `if` | 105, 102 | 1101001, 1100110 | U+0069, U+0066 | Comprehension filter (already have) |

## Import Keywords
Import statement keywords (already mostly have).

| Keyword | Ords | Binary | Unicode | Description |
|---------|------|--------|---------|-------------|
| `import` | 105, 109, 112, 111, 114, 116 | 1101001, 1101101, 1110000, 1101111, 1110010, 1110100 | U+0069, U+006D, U+0070, U+006F, U+0072, U+0074 | Import module (already have) |
| `from` | 102, 114, 111, 109 | 1100110, 1110010, 1101111, 1101101 | U+0066, U+0072, U+006F, U+006D | From import (already have) |
| `as` | 97, 115 | 1100001, 1110011 | U+0061, U+0073 | Alias import (already have) |

## Async/Await Keywords
Asynchronous execution keywords.

| Keyword | Ords | Binary | Unicode | Description |
|---------|------|--------|---------|-------------|
| `async` | 97, 115, 121, 110, 99 | 1100001, 1110011, 1111001, 1101110, 1100011 | U+0061, U+0073, U+0079, U+006E, U+0063 | Async function/context |
| `await` | 97, 119, 97, 105, 116 | 1100001, 1110111, 1100001, 1101001, 1110100 | U+0061, U+0077, U+0061, U+0069, U+0074 | Await coroutine result |

## Type-Related Keywords
Keywords for type checking and type hints.

| Keyword | Ords | Binary | Unicode | Description |
|---------|------|--------|---------|-------------|
| `isinstance` | 105, 115, 105, 110, 115, 116, 97, 110, 99, 101 | 1101001, 1110011, 1101001, 1101110, 1110011, 1110100, 1100001, 1101110, 1100011, 1100101 | U+0069, U+0073, U+0069, U+006E, U+0073, U+0074, U+0061, U+006E, U+0063, U+0065 | Check instance type (built-in, but scope-relevant) |
| `issubclass` | 105, 115, 115, 117, 98, 99, 108, 97, 115, 115 | 1101001, 1110011, 1110011, 1110101, 1100010, 1100011, 1101100, 1100001, 1110011, 1110011 | U+0069, U+0073, U+0073, U+0075, U+0062, U+0063, U+006C, U+0061, U+0073, U+0073 | Check subclass (built-in, but scope-relevant) |
| `type` | 116, 121, 112, 101 | 1110100, 1111001, 1110000, 1100101 | U+0074, U+0079, U+0070, U+0065 | Get type (built-in, but scope-relevant) |

## Comprehension Types (Create Local Scopes)
These create new local scopes and need special handling.

```
[x for x in ...]        # List comprehension
{k: v for k, v in ...}  # Dict comprehension
{x for x in ...}        # Set comprehension
(x for x in ...)        # Generator expression
```

## Special Considerations

### Multi-Word Operators/Keywords (Already Have Some)
```
not in      # Negative membership (already have)
is not      # Negative identity (already have)
yield from  # Generator delegation (listed above)
async def   # Async function definition
```

### Context-Dependent Operators
- `*` appears as: multiplication, unpacking, wildcard import
- `**` appears as: exponentiation, unpacking, kwargs
- `:` appears as: type hint, slice separator, dict separator
- `@` appears as: decorator, matrix multiplication
- `/` appears as: division, positional-only parameter separator (Python 3.8+)

### Edge Cases
- Decorators can stack: `@decorator1` `@decorator2`
- Type hints on variables: `x: int = 5`
- Walrus in conditionals: `if (x := func()):`
- Slice with step: `[start:stop:step]`
- Extended slices: `array[x:y, z:w]`
- Multiple assignment: `a = b = c = 1`
- Tuple unpacking: `a, b = 1, 2`
- Starred unpacking: `a, *b, c = values`

### String Quote Variations
```
'text'          # Single quote
"text"          # Double quote
'''text'''      # Triple single quote
"""text"""      # Triple double quote
f'text'         # f-string
r'text'         # Raw string
b'text'         # Bytes
u'text'         # Unicode (Python 2 legacy)
```

## Organization Suggestion for Config

Based on the above, consider these top-level categories:

1. **Assignment Operators** - All forms of assignment
2. **Annotation Operators** - Type hints
3. **Unpacking Operators** - `*`, `**`
4. **Separators** - `,`, `:`, `...`
5. **Scope Declaration** - `global`, `nonlocal`, `lambda`, `del`, `pass`
6. **Control Flow** - `break`, `continue`, `return`, `yield`, `assert`, `raise`
7. **String Prefixes** - `f`, `r`, `b`, `u`, and combinations
8. **Context Management** - `with`, `as`
9. **Exception Handling** - `try`, `except`, `else`, `finally`
10. **Async/Await** - `async`, `await`
11. **Comprehensions** - Local scope keywords: `for`, `in`, `if`
12. **Imports** - `import`, `from`, `as`

## Implementation Notes for Tracking and Tests

- Keep the existing operator and keyword inventories as source references.
- Build test fixtures from the generator in `pyparsingconfig.py` instead of hand-maintained tables.
- Validate each token row with these assertions:
	- `len(ords) == length_chars`
	- `len(binary) == len(ords)`
	- `len(unicode) == len(ords)`
	- `len(hexadecimal) == len(ords)`
	- `len(octal) == len(ords)`
	- `len(utf8_bytes) == length_bytes`
- For multi-word tokens (`yield from`, `not in`, `is not`, `async def`), ensure whitespace flags are true.
