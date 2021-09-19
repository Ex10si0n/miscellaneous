function HuffmanTreeNode(val, lch, rch) {
    this.val = val;
    this.lch = lch;
    this.rch = rch;
}

function HuffmanTree(root) {
    this.root = root;
}

function frequencyCounter(text) {
    var dict = {};
    for (var i = 0; i < text.length; i++) {
        dict[text[i]] ? dict[text[i]]++ : dict[text[i]] = 1;
    }
    return dict;
}

function sortNumber(a, b) {
    return a - b;
}

function process(text) {
    var frequencyDict = frequencyCounter(text);
    // frequencyDict.sortByValue
    var sortedFrequencies = {};
    for (var j = 0; j < frequencyDict.length; j++) {
        var char, minimum;
        for (var i = 0; i < frequencyDict.length; i++) {
            minimum = frequencyDict[0];
            if (frequencyDict[i].value < minimum) {
                minimum = frequencyDict[i].value;
                char = frequencyDict[i].key;
            }
        }
        sortedFrequencies[char] = minimum;
    }
}

$(function () {
    $("#btn").on("click", function() {
        var text = $("#text").val();
        var encode = process(text);
        $("#encode").val(encode);
    });
});

