# Assignment 2 - Core Modules

**Question 1:** What’s Box Model in CSS ?
**Answer:**
> The Box Model in CSS is a design layout which specifies the layout, spacing and size of elements on a web page.
These 4 properties are part of the CSS Box Model which define the layout & design of the html element. => Content, Padding, Border & Margin
Content is the actual content inside the element.
Padding is the spacing between content and the border.
Border is the boundary / end part of the element that encloses the content and padding layout of the element.
Margin is the spacing between the border of an element and other elements, it provides visual spacing of elements between each other.


**Question 2:** What are the Different Types of Selectors in CSS & what are the advantages of them?
**Answer:**
> These are the following types of CSS selectors.
> - .class-selector => Selects all html elements containing the exact class name
> - \#id-selector => Selects the html element containing the exact id name (Must be unique across html page.)
> - h1 => Element selector => Selects all the occurrences of the html element.
> - [class=”based”] => Selects all the occurrences of those html elements that have the exact attribute name and exact value.
> - * => Selects ‘all’ the elements, its descendants and children in the html document.

**Question 3:** What is VW/VH ?
**Answer:**
> The Viewport is that part of the web page that is visible to the user. 
Viewport width (VW) and Viewport height (VH) are CSS properties that may be used to specify the Width and Height of an element ‘relative’ to the size of a web page’s viewport height and width. On the other hand pixels (px) is a fixed unit of length based on the device’s pixel resolution. So if we specify in px we are hardcoding the size value of the element and it will remain the exact same across all sizes of devices.


**Question 4:** Whats difference between Inline, Inline Block and block ?
**Answer:**
> - Block => An element’s display set to block will make it occupy all the horizontal space on the web page, meaning another element cannot be next to it or on the same line.
> - Inline => An element’s display set to inline will make it occupy only the necessary space required and other elements can be next to it or on the same line.
> - Inline-Block => An element’s display set to inline will make it display like an Inline element but with a little bit of margin across all its sides, including top & bottom


**Question 5:** How is Border-box different from Content Box?
**Answer:**
> - If you specify box sizing of an element to content-box, it will keep the sizes of all of the box model’s properties separate and add it on top of the content’s width and height. If for example, the width & height of content is 100px and padding is 20px, then 20px is added on top of the content and final size of the element comes to 120px
> - If you specify the box sizing of an element to border-box, it will account for / include the sizes of box model’s properties (border, padding) within content’s width & height. Hence if the padding is 20px, it will fit inside the content and the content size will shrink to 80px. This typically makes it much easier to size elements. As we usually dictate the size of any html element by its content’s size, not padding and border.

**Question 6:** What’s z-index and How does it Function ?
**Answer:**
> In css the z-index property will determine the order of display priority of elements that are positioned on top of each other. If the z-index of element A is 1 and element B is 0, then element A will show above element B if they are overlapping each other. It positions elements in the z-axis and layers them on top of each other.

**Question 7:** What’s Grid & Flex and difference between them?
**Answer:**
> - CSS Flexbox model displays the elements in such a way that it tries to distribute equal free space between each and every element and the directional alignment can be easily set up using other css properties such as align-items and justify-content. It’s a great choice for responsive designs.
> - The CSS Grid model uses a grid based layout, and places the elements in fixed size grids spanning across rows and columns. It’s pretty much like a table except we have more control over how we want to keep the design of rows and columns such as total rows / columns, span, grid elements alignment & etc.


**Question 8:** Difference between absolute and relative and sticky and fixed position explain with example.
**Answer:**
> In the simplest words, the CSS has a property called the ‘position’ property, which decides the position of the current element on the UI page’s flow. There are 5 positions which we can choose from.
> - Static: All HTML elements are statically positioned by default. This position prevents the element from being moved by directional properties (such as left, right, top & bottom). It will be positioned as with the flow of the UI’s elements.
> - Relative: The element which is relatively positioned, means it will be movable, relative to its actual position where it should have been if it weren’t moved manaully.
> - Fixed: The element will stay on the screen of the user’s web page all the time! Except it will be able to be moved around the screen to adjust its position.
> - Absolute: The element which is absolutely positioned, means it will be movable, relative to its nearest parent element’s position, which is relatively positioned. So, if there are no elements that are relatively positioned, then the element will be positioned according to the document page’s body. This is the usual behavior for which absolute position is used to move an element, regardless of its parent element’s position.
> - Sticky: The element will stay on the screen even if the user's scroll position is fixed. But it will be movable around the screen, and until it reaches the end/side of the body, it will stay there as it’s sticky positioned. Useful for making Navbars/Panels stick on the page even if they are scrolled out of their viewport/position.

**Question 9:** Build Periodic Table as shown in the below image
![Image.png](https://pwskills.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F41470e09-2a72-448e-b080-ed9ede4b3c76%2Fperiodic_table.png?id=769a10d4-c2ba-4af0-8de5-28bee2644c3f&table=block&spaceId=6fae2e0f-dedc-48e9-bc59-af2654c78209&width=1440&userId=&cache=v2)
**Answer:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solution to question 19</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="upper-section center">
        <div class="column red">
            <div class="element center">1 H</div>
            <div class="element center">3 LI</div>
            <div class="element center">11 Na</div>
            <div class="element center">19 K</div>
            <div class="element center">37 Rb</div>
            <div class="element center">55 Cs</div>
            <div class="element center">87 Fr</div>
        </div>
        <div class="column red">
            <div class="element center">4 Be</div>
            <div class="element center">12 Mg</div>
            <div class="element center">20 Ca</div>
            <div class="element center">38 Sr</div>
            <div class="element center">56 Ba</div>
            <div class="element center">88 Ra</div>
        </div>
        <div class="column blue">
            <div class="element center">21 Sc</div>
            <div class="element center">39 Y</div>
            <div class="element center">71 Lu</div>
            <div class="element center">103 Lr</div>
        </div>
        <div class="column blue">
            <div class="element center">22 Ti</div>
            <div class="element center">40 Zr</div>
            <div class="element center">72 Hf</div>
            <div class="element center">104 Rf</div>
        </div>
        <div class="column blue">
            <div class="element center">23 V</div>
            <div class="element center">41 Nb</div>
            <div class="element center">73 Ta</div>
            <div class="element center">105 Db</div>
        </div>
        <div class="column blue">
            <div class="element center">24 Cr</div>
            <div class="element center">42 Mo</div>
            <div class="element center">74 W</div>
            <div class="element center">106 Sg</div>
        </div>
        <div class="column blue">
            <div class="element center">25 Mn</div>
            <div class="element center">43 Tc</div>
            <div class="element center">75 Re</div>
            <div class="element center">107 Bh</div>
        </div>
        <div class="column blue">
            <div class="element center">26 Fe</div>
            <div class="element center">44 Ru</div>
            <div class="element center">76 Os</div>
            <div class="element center">108 Hs</div>
        </div>
        <div class="column blue">
            <div class="element center">27 Co</div>
            <div class="element center">45 Rh</div>
            <div class="element center">77 Ir</div>
            <div class="element center">109 Mt</div>
        </div>
        <div class="column blue">
            <div class="element center">28 Ni</div>
            <div class="element center">46 Pd</div>
            <div class="element center">78 Pt</div>
            <div class="element center">110 Ds</div>
        </div>
        <div class="column blue">
            <div class="element center">29 Cu</div>
            <div class="element center">47 Ag</div>
            <div class="element center">79 Au</div>
            <div class="element center">111 Rg</div>
        </div>
        <div class="column blue">
            <div class="element center">30 Zn</div>
            <div class="element center">48 Cd</div>
            <div class="element center">80 Hg</div>
            <div class="element center">112 Cn</div>
        </div>
        <div class="column yellow">
            <div class="element center">5 B</div>
            <div class="element center">13 Ai</div>
            <div class="element center">31 Ga</div>
            <div class="element center">49 In</div>
            <div class="element center">81 Ti</div>
            <div class="element center">113 Nh</div>
        </div>
        <div class="column yellow">
            <div class="element center">6 C</div>
            <div class="element center">14 Si</div>
            <div class="element center">32 Ge</div>
            <div class="element center">50 Sn</div>
            <div class="element center">82 Pb</div>
            <div class="element center">114 Fi</div>
        </div>
        <div class="column yellow">
            <div class="element center">7 N</div>
            <div class="element center">15 P</div>
            <div class="element center">33 As</div>
            <div class="element center">51 Sb</div>
            <div class="element center">83 Bi</div>
            <div class="element center">115 Mc</div>
        </div>
        <div class="column yellow">
            <div class="element center">8 O</div>
            <div class="element center">16 S</div>
            <div class="element center">34 Se</div>
            <div class="element center">52 Te</div>
            <div class="element center">84 Po</div>
            <div class="element center">116 Lv</div>
        </div>
        <div class="column yellow">
            <div class="element center">9 F</div>
            <div class="element center">17 Cl</div>
            <div class="element center">35 Br</div>
            <div class="element center">53 I</div>
            <div class="element center">85 At</div>
            <div class="element center">117 Ts</div>
        </div>
        <div class="column yellow">
            <div class="element center" style="background-color: #FF6969;">2 He</div>
            <div class="element center">10 Ne</div>
            <div class="element center">18 Ar</div>
            <div class="element center">36 Kr</div>
            <div class="element center">54 Xe</div>
            <div class="element center">86 Rn</div>
            <div class="element center">118 Og</div>
        </div>
    </div>
    <div class="lower-section green">
        <div class="element center">57 La</div>
        <div class="element center">58 Ce</div>
        <div class="element center">59 Pr</div>
        <div class="element center">60 Nd</div>
        <div class="element center">61 Pm</div>
        <div class="element center">62 Sm</div>
        <div class="element center">63 Eu</div>
        <div class="element center">64 Gd</div>
        <div class="element center">65 Tb</div>
        <div class="element center">66 Dy</div>
        <div class="element center">67 Ho</div>
        <div class="element center">68 Er</div>
        <div class="element center">69 Tm</div>
        <div class="element center">70 Yb</div>
        <div class="element center">89 Ac</div>
        <!-- Bottom row -->
        <div class="element center">90 Th</div>
        <div class="element center">91 Pa</div>
        <div class="element center">92 U</div>
        <div class="element center">93 Np</div>
        <div class="element center">94 Pu</div>
        <div class="element center">95 Am</div>
        <div class="element center">96 Cm</div>
        <div class="element center">97 Bk</div>
        <div class="element center">98 Cf</div>
        <div class="element center">99 Es</div>
        <div class="element center">100 Fm</div>
        <div class="element center">101 Md</div>
        <div class="element center">102 No</div>
    </div>
</body>
</html>
```
```css
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

body {
    width: 100%;
    height: 100vh;
    flex-direction: column;
    background-color: #9DB2BF;
}

.center, body {
    display: flex;
    align-items: center;
    justify-content: center;
}

.upper-section {
    align-items: flex-end;
}

.element {
    margin: 0.25rem;
    border: 2px solid black;
    overflow: hidden;

    width: 40px;
    height: 40px;
    text-align: center;

    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 1rem;
    font-weight: 500;
}

.red > div {
    background-color: #FF6969;
}

.blue > div {
    background-color: #99ccff;
}

.yellow > div {
    background-color: #fdff8c;
}

.green > div {
    background-color: #9bff99;
}

.lower-section {
    display: grid;
    margin-top: 1rem;

    grid-template-rows: repeat(2, auto);
    grid-template-columns: repeat(14, auto);
}
```

**Question 10:** Build Responsive Layout both desktop and mobile and Tablet, see below image for reference?
![Image.png](https://pwskills.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fa884c074-bb09-4827-a38f-290726e97f64%2Fresponsive.jpg?id=1174eb35-8bb2-41cf-aee6-376b8890092c&table=block&spaceId=6fae2e0f-dedc-48e9-bc59-af2654c78209&width=1200&userId=&cache=v2)
**Answer:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solution to question 20</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>Header</header>
    <main>
        <aside>Aside</aside>
        <article>
            <p>Article</p>
            <div class="images">
                <div>Image</div>
                <div>Image</div>
                <div>Image</div>
            </div>
        </article>
    </main>
</body>
</html>
```
```css
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;

    color: white;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    font-size: 28px;
}

body {
    width: 100%;
    height: 100vh;
    background-color: #c4ebf9;
    overflow: hidden;
}

header {
    width: 95%;
    height: 15%;
    background-color: #02bfb1;
    margin: 1rem auto;
}

main {
    width: 95%;
    height: 75%;
    margin: 1rem auto;

    display: grid;
    grid-template-columns: repeat(3fr, auto);
}

aside {
    height: 100%;
    grid-column: 1;
    background-color: #6edb6e;
    margin-right: 1rem;
}

article {
    height: 100%;
    grid-column: 2 / span 2;
    background-color: #fbb04c;
    margin-left: 1rem;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-end;
}

.images {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    padding: 0.5rem 0;
}

.images div {
    width: 30%;
    height: 10rem;
    background-color: #fcd24a;
}

header, aside, .images div {
    display: flex;
    align-items: center;
    justify-content: center;
}
```
