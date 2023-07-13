# Assignment 1 - Core Modules

**Question 1:** \<!DOCTYPE html> is it a tag of html? If not, what is it and why do we use it?
**Answer:**
> \<!DOCTYPE html> is something that must be mentioned at the top of every html file to instruct the browsers to render the following html content using certain specifications. If this part is not mentioned in .html files, then the browsers will attempt to render the site content in their own way (which could cause compatibility issues)
> \<!DOCTYPE html> is not a tag of html, it’s like a code that instructs the browser to render the content using HTML 5 specifications. HTML 5 version is the latest browser specification version.

**Question 2:** Explain Semantic tags in html? And why do we need it?
**Answer:**
> Semantics tags in html are those tags that give the content enclosed inside the tags a ‘different’ meaning. For example a \<h1> tag in html will indicate that it is a “top level header” in the page. And so the browsers will treat it as a top level header and give it a big font size.
This explains why we have so many element tags in html when our work can simply be done using div tags. However, each and every tag interprets the given text / content in a different way so that each of these parts can be described meaningfully. It is also advantageous to use the right, proper semantic html tags to suggest what type of data we should put there, for SEO, web scraping and for proper tags naming.
Examples of semantic tags in html  are, h1-h6, article, aside, img, nav, main, header, footer, form, article.

**Question 3:** Differentiate between HTML Tags and Elements?
**Answer:**
> \<h1> ⇐ Anything that is written inside those Angular (<>) brackets is called as Html tags.
\<h1>Hello World!\</h1> Anything that is between those html tags is called as Html elements.

![Image.png](https://media.discordapp.net/attachments/1125577671481503755/1128636432026697851/image.png?width=538&height=292)

**Question 4:** Build Your Resume using HTML only
**Answer:** ...

**Question 5:** Write HTML code so that it looks like the below image
**Answer:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solution to question 5</title>
</head>
<body>
    <img src="./AdobeStock_211303600_Preview.jpeg" alt="woman using laptop on desk" height="360px" width="auto">
    <p>We will be learning the following things this week</p>
    <table>
        <tr>
            <th>Day 1</th>
            <th>Day 2</th>
            <th>Day 3</th>
            <th>Day 4</th>
        </tr>
        <tr>
            <td>Linux 1</td>
            <td>HTML</td>
            <td>Linux 2</td>
            <td>Linux 3</td>
        </tr>
        <tr>
            <td>Git 1</td>
            <td>CSS</td>
            <td>Git 2</td>
            <td>Bootstrap</td>
        </tr>
    </table>
    <p>If you want to contact me, please fill in this form</p>
    <form>
        <div>
            <label for="name">Name:</label><br>
            <input type="text" name="name" id="name">
        </div>
        <div>
            <label for="phno">Phone No:</label><br>
            <input type="text" name="phno" id="phno">
        </div>
        <div>
            <label for="email">Email Id:</label><br>
            <input type="text" name="email" id="email">
        </div>
    </form>
    <br>
    <h3>The following things are important to be a programmer</h3>
    <ul>
        <li>A problem solving mindset</li>
        <li>Consistency</li>
        <ul>
            <li>Clean code</li>
            <li>Thorough knowledge of core concepts</li>
            <li>Readable code</li>
        </ul>
        <li>Speed</li>
    </ul>
</body>
</html>
```

**Question 6:** What are some of the advantages of HTML5 over its previous versions?
**Answer:**
> HTML 4 is the 4th iteration (or we can say version) of HTML. HTML 5 is the latest HTML iteration that is currently there in modern web development; these iterations specify instructions and features that shall be implemented by browsers for better user experience.
In short, HTML 5 should be used by every developer when creating a new website.
HTML 5 introduces the following features and specifications that were not present in older HTML versions (eg Html 4 and Html 3):
Easily specify HTML version declaration using \<!DOCTYPE html>
New Html tags such as \<audio>, \<video>, \<header> & \<footer> etc.
Better syntax handling
New \<canvas> element for 3d rendering and game development
Geo-location support
SEO benefits & etc.

**Question 7:** Create a simple Music player using html only
**Answer:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solution to question 7</title>
</head>
<body>
    <figure>
        <audio controls>
            <source src="./Thunder - Imagine Dragons.mp3" type="audio/mpeg">
        </audio>
        <figcaption>Thunder - Imaging Dragons</figcaption>
    </figure>
</body>
</html>
```

**Question 8:** What is the difference between \<figure> tag and \<img> tag?
**Answer:**
> \<img> tag is used to render an image on the web browser by passing a local image path or an image url to its src attribute. This tag has the sole purpose to render images hence it cannot be used to enclose / render anything else.

> \<figure> tag is used to enclose multimedia content or an illustration. \<figure> is used in combination with \<figcaption> to optionally give a caption to the multimedia content / illustration that is being rendered on the browser. The purpose of the \<figure> tag is to give a semantic meaning to the contents contained inside of it so that web scrapers can understand that this particular element contains content such as Image, Video, Codeblock and the text inside figcaption is describing this particular content.

> As an example, \<figure> tag is mostly used to enclose an \<img> tag and \<figcaption> tag together so that it’s clear to everyone that the Image is a multimedia / illustration and figcaption describes it.

**Question 9:** What’s the difference between html tag and attribute and give example of some global attributes?
**Answer:**
> \h1> ⇐ This is called an Html tag.
\h1 class=”heading-1” id=”heading-1” style=”font-size:56px;” > The parts between the `h1` tag and the angular bracket `>` are the attributes of an Html tag. These attributes’ anatomy is ‘key=value’ where the left side of = is the name of the attribute and the right side of = is the value in a string form.
Html attributes provide additional styling to the html element.
Some attributes can be found in each and every type of html element tags. These are called global attributes.
Examples of global attributes: class, id, style, hidden, etc.

Question 10: Write Html code so that it looks like the below image
![Image.png](https://pwskills.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F365d0427-ccce-4f03-8f68-f71394cb86b5%2FUntitled.png?id=bc83e227-e490-4173-966b-be20296428d1&table=block&spaceId=6fae2e0f-dedc-48e9-bc59-af2654c78209&width=1320&userId=&cache=v2)
**Answer:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solution to question 10</title>
</head>
<body>
    <table border="1px solid green;" style="width: 400px; height: 100px; text-align: center;">
        <tr>
            <th rowspan="3">Day</th>
            <th colspan="3">Seminar</th>
        </tr>
        <tr>
            <th colspan="2">Schedule</th>
            <th rowspan="2">Topic</th>
        </tr>
        <tr>
            <th>Begin</th>
            <th>End</th>
        </tr>
        <tr>
            <td rowspan="2">Monday</td>
            <td rowspan="2">8:00 am</td>
            <td rowspan="2">5:00 pm</td>
            <td>Introduction to XML</td>
        </tr>
        <tr>
            <td>Validity : DTD and Relax NG</td>
        </tr>
        <tr>
            <td rowspan="3">Tuesday</td>
            <td>8:00 am</td>
            <td>11:00 am</td>
            <td rowspan="3">XPath <hr> XSL Transformations</td>
        </tr>
        <tr>
            <td>11:00 am</td>
            <td>2:00 pm</td>
        </tr>
        <tr>
            <td>2:00 pm</td>
            <td>5:00 pm</td>
        </tr>
        <tr>
            <td>Wednesday</td>
            <td>8:00 am</td>
            <td>12:00 pm</td>
            <td>XSL Formatting Objects</td>
        </tr>
    </table>
</body>
</html>
```
