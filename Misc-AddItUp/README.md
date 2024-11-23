# Add It Up

##  Misc

### You got to add it up, add it up....  And here's some code to help.

The code shows two things: 1) everytime it goes through the loop the timer increase exponentially `totaltime = pow(2, i)`, and 2) it uses a Python slice `[:]` to print the number of characters corresponding to the number entered for questions.

So if you think inside the box, after about 6 questions it will take forever to print the flag.  As an example, To get the 20 characters, the time between the 19th and 20th would take over 12 days.

```sh
pow(2, 20) / 60 / 60 /24
12.136296296296296
```

So, looking at the second interesting piece of the code, if you use a negative number, 1) it won't enter the loop, and 2) it will print all but the last character.

```python
>>> "a_string"[:-1]
'a_strin'
>>> "a_string\n"[:-1]
'a_string'
>>> 
```

```sh
$  nc web.teractf.com 2225 
How many questions would you like to answer? -1

teractf{y0u_kn0w_U_g0t_my_5ymp4thy!!!}
```

**teractf{y0u_kn0w_U_g0t_my_5ymp4thy!!!}**

