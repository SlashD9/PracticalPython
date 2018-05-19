/* 
// This is to show the answer on screen
// I may use this in the future to show when a numbered amount of attempts have been tried

function show_answer() {
    document.getElementById("answer").style.display = "block";
}
 */

var x = 0;
var array = Array();

function add_element_to_array() {
    array[x] = document.getElementById("answer").value;
    console.log(array[x])
    x++;
    document.getElementById("answer").value = "";
    display_array();
};

function display_array() {
    var e = "<hr/>";   
    
    for (var y=0; y<array.length; y++)
    {
     e += "Element " + y + " = " + array[y] + "<br/>";
    }
    document.getElementById("Result").innerHTML = e;
};