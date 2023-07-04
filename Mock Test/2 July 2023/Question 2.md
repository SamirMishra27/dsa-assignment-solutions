### 2. Create a form with basic validation (name, email, phone number, password, age, gender, date, color picker)
---
**Answer**
```html

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Document</title>
  </head>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    body {
      background-color: aliceblue;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
      font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS",
        sans-serif;
    }
    input,
    select {
      width: 10rem;
      height: 24px;
      border-radius: 4px;
      padding: 0.25rem;
      margin-bottom: 1rem;
    }
  </style>
  <body>
    <form action="">
      <label for="NAME">NAME</label>
      <input type="text" name="NAME" id="NAME" />
      <br />

      <label for="EMAIL">EMAIL</label>
      <input type="email" name="EMAIL" id="EMAIL" />
      <br />

      <label for="PHONE">PHONE NO</label>
      <input type="tel" name="PHONE" id="PHONE" />
      <br />

      <label for="PASSWORD">PASSWORD</label>
      <input type="password" name="PASSWORD" id="PASSWORD" />
      <br />

      <label for="AGE">AGE</label>
      <input type="number" name="AGE" id="AGE" maxlength="2" />
      <br />

      <label for="GENDER">GENDER</label>
      <select name="GENDER" id="GENDER">
        <option value="MALE">MALE</option>
        <option value="FEMALE">FEMALE</option>
        <option value="NON BINARY">NON BINARY</option>
      </select>
      <br />

      <label for="DATE">DATE</label>
      <input type="date" name="DATE" id="DATE" />
      <br />

      <label for="COLOR">COLOR</label>
      <input type="color" name="COLOR" id="COLOR" />
      <br />
    </form>
  </body>
</html>
```

Output:
![](https://media.discordapp.net/attachments/1125577671481503755/1125596487628357712/image.png?width=529&height=605)