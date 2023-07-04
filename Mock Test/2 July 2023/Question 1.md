### 1. Explain all the CSS positions(static, fixed, sticky, relative, absolute) with one code example each
-----
**Answer**
> **Static:** All HTML elements are statically positioned by default. This position prevents the element from being moved by directional properties (such as left, right, top & bottom). It will be positioned as with the flow of the UI’s elements.

Example:
```html
<body>
  <div class="static-element">
      Hello world!
  </div>
  <div class="static-element">
      Hello Html!
  </div>
</body>
```
```css
.static-element {
    width:  100px;
    height: 100px;
    color: brown;
    left: 1000px;   /* Will not work! */
    right: 500px;   /* Will not work! */
}
```
Output:
![](https://media.discordapp.net/attachments/1125577671481503755/1125577680960618546/image.png?width=482&height=376)

---
**Relative:** The element which is relatively positioned, means it will be movable, relative to its actual position where it should have been if it weren’t moved manually.

Example:
```html
<body>
  <div class="element static">
    Hello world!
  </div>
  <div class="element relative">
    Hello Html!
  </div>
</body>
```
```css
.element {
  width: 100px;
  height: 100px;
  background-color: brown;
  color: white;
  left: 100px; /* Will not work! */
  right: 50px; /* Will not work! */
}
.relative {
  position: relative;
}
```
Output:
![](https://media.discordapp.net/attachments/1125577671481503755/1125579445810499614/image.png?width=755&height=463)

---
**Fixed:** The element will stay on the screen of the user’s web page all the time! Except it will be able to be moved around the screen to adjust its position.

Example:
```html
<body>
  <div class="element fixed">
    This won't go out of screen!
  </div>
  <div class="element static">
    Hello world!
  </div>
  <div class="element static">
    Hello world!
  </div>
  <div class="element static">
    Hello world!
  </div>
  <div class="element static">
    Hello world!
  </div>
  <div class="element relative">
    Hello Html!
  </div>
  <div class="element relative">
    Hello Html!
  </div>
  <div class="element relative">
    Hello Html!
  </div>
  <div class="element relative">
    Hello Html!
  </div>
</body>
```
```css
.element {
  width: 100px;
  height: 100px;
  background-color: brown;
  color: white;
  left: 100px; /* Will not work! */
  right: 50px; /* Will not work! */
}
.relative {
  position: relative;
}
.fixed {
  background-color: yellowgreen;
  position: fixed;
  left: 250px;
}
```
Output:
![](https://media.discordapp.net/attachments/1125577671481503755/1125580864345092106/image.png?width=588&height=605)
![](https://media.discordapp.net/attachments/1125577671481503755/1125580864697417758/image.png?width=593&height=605)

---
**Absolute:** The element which is absolutely positioned, means it will be movable, relative to its nearest parent element’s position, which is relatively positioned. So, if there are no elements that are relatively positioned, then the element will be positioned according to the document page’s body. This is the usual behavior for which absolute position is used to move an element, regardless of its parent element’s position.

Example:
```html
<body>
  <div class="body-child">
    My relative parent is body
  </div>
  <div class="relative-parent">
    <div class="relative-child">
      My relative parent is relative-parent
    </div>
  </div>
</body>
```
```css
.body-child {
  height: 10rem;
  width: 10rem;
  background-color: aquamarine;
  position: absolute;
  bottom: 12rem;
}
.relative-parent {
  height: 10rem;
  width: 10rem;
  background-color: seagreen;
  position: relative;
}
.relative-child {
  height: 5rem;
  width: 5rem;
  background-color: cadetblue;
  position: absolute;
  bottom: 20px;
  right: 20px;
}
```
Output:
![](https://media.discordapp.net/attachments/1125577671481503755/1125583392734445670/image.png?width=558&height=605)

---
**Sticky:** The element will stay on the screen even if the user's scroll position is fixed. But it will be movable around the screen, and until it reaches the end/side of the body, it will stay there as it’s sticky positioned. Useful for making Navbars/Panels stick on the page even if they are scrolled out of their viewport/position.


Example:
```html
<body>
  <nav>Welcome to codesandbox.io!</nav>
  <article>
    This is a long article! Lorem ipsum dolor sit
amet consectetur,
    adipisicing elit. Facilis aspernatur vitae 
illo omnis corporis tenetur
    quod obcaecati tempora iure officiis 
voluptatibus sed ratione vero ducimus
    odit voluptate, incidunt unde. Non iste quae 
aliquam obcaecati esse id
    quia quibusdam nesciunt sit quis, dolores hic
adipisci voluptate beatae
    cum, atque enim? Velit eos nesciunt itaque 
officiis dicta blanditiis in
    quo autem voluptatibus, adipisci aspernatur 
fugit ipsum? Nobis
    necessitatibus velit neque adipisci eum quo 
ea magnam pariatur a!
    Explicabo, tempora? Iste quae totam hic 
commodi modi ut porro ad inventore
    est, adipisci incidunt ab, consectetur 
facilis sed aperiam. Eius,
    temporibus aspernatur? Aperiam earum nemo 
quaerat dolores, velit ipsam
    exercitationem, molestias quia illum eos quis
fuga ab debitis incidunt id
    possimus asperiores facere natus dignissimos 
vero totam hic suscipit
    adipisci atque! Deserunt quibusdam voluptate 
officiis soluta voluptas
    laborum quisquam, inventore reiciendis, 
eveniet itaque quod.
  </article>
```
```css
nav {
  width: 100%;
  height: 4rem;
  position: sticky;
  top: 0px;
  background-color: coral;
  text-align: center;
  font-size: 20px;
}
article {
  padding: 4rem;
  background-color: floralwhite;
  font-size: 24px;
  text-align: justify;
}
```
Output:
![](https://media.discordapp.net/attachments/1125577671481503755/1125586088346525707/image.png?width=561&height=605)
![](https://media.discordapp.net/attachments/1125577671481503755/1125586088698851420/image.png?width=584&height=605)

This describes all the CSS position properties.