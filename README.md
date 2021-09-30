# Oneliner  
Oneliner is a simple python script that turns your code into one line.  

- **Why?**  

> Because why not?  

- **How does it work?**  

> It detects the linebreaks and indents and replaces them with \n and \t respectively, then executes the result by using built-in function "exec()".

### Example:   

- Input:   

```python
value_a=0
value_b=1
i=3
j=10
for z in range(j):
    result = value_a + value_b
    if i <= z <= j:
        print(result)
    value_a = value_b
    value_b = result
```

- Output:  

```python
exec("value_a=0\nvalue_b=1\ni=3\nj=10\nfor z in range(j):\n\tresult = value_a + value_b\n\tif i <= z <= j:\n\t\tprint(result)\n\tvalue_a = value_b\n\tvalue_b = result")
```

- Output of both:
```python
5
8
13
21
34
55
89
```
