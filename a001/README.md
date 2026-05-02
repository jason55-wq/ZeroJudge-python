# ZeroJudge a001 - 哈囉

## 題目說明

輸入一個字串，並輸出 `hello, ` 加上該字串。

例如輸入：

```text
world
```

輸出：

```text
hello, world
```

## 輸入說明

輸入總共一行，包含一組文字。

## 輸出說明

輸出題目指定的文字格式：

```text
hello, 輸入的文字
```

## 範例輸入 1

```text
world
```

## 範例輸出 1

```text
hello, world
```

## 範例輸入 2

```text
C++
```

## 範例輸出 2

```text
hello, C++
```

## 範例輸入 3

```text
Taiwan
```

## 範例輸出 3

```text
hello, Taiwan
```

## Python 解法

```python
a = input()
print("hello,", a)
```

## 解題想法

這題只需要讀取一行輸入，然後按照題目要求的格式輸出。

使用 `input()` 讀入字串，再用 `print()` 輸出 `hello,` 和輸入的文字。
