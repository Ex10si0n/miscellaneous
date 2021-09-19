# Notes on `jQuery`

## Basic

### Grammar

jQuery selects a specific HTML element and do some actions on this.

```javascript
$(selector).action()

// Example
$(function () {
    #("c1").on("click", function () {
        $(".toggleable").hide();
    });
});
```
selector could be `this`, `p`, `id`, and `class` 

All jQuery functions should be included in "document ready"

```javascript
$(document).ready(function () {
    // some codes here
});

// or simplified as

$(function () {
    // some codes here
});
```

### Selectors

Basic module has introduced the `selector`. Specifically, 
the instances are listed as below:

```javascript
$("*")                      // All
$(this)                     // this Object
$("p.intro")                // p.class -> .intro
$("p:first")                // document -> first element <p>
$("ul li:first")            // first <ul> -> first <li>
$("ul li:first-child")      // each <ul> -> first <li>
$("[href]")                 // all elements with `href` attribute
$("a[target='_blank']")     // all <a> with `target=_blank`
$("a[target!='_blank']")    // all <a> without `target=_blank`
$(":button")                // all button like elements 
                            // including <input type="button">
$("tr:even")                // even <tr>
$("tr:odd")                 // odd <tr>
```

### Events

Common DOM Events

```javascript
$(this).on("click", function () { /* code here */ });     // -> onclick()
hover     // -> css.hover
keydown   // -> onkeydown()
keyup     // -> onkeyup()
submit    // k-> onsubmit()
load      // -> onload()
```

### Effects

some useful jQuery effects are listed below:

#### Toggle

```javascript
$("#c1").on("click", function () {
    $(".toggleable").toggle();
});
```

#### Fade in / Fade out

```javascript
$("button").on("click", function () {
    $("#div1").fadeIn().fadeTo("slow", 0.15);
    $("#div2").fadeIn("slow").fadeTo("slow", 0.15);
    $("#div3").fadeIn(1000).fadeTo("slow", 0.15);
});
```

### Slide Toggle

```javascript
$("#slide").on("click", function () {
    $("#panel").slideToggle("slow");
});
```