function sayHello() {
    document.write("Hello Folks! <br>");
}
sayHello();
 function sayHelloWithParams(firstName, lastName = 'Done') {
    document.write("Hello" + firstName + " " + "! <br>");
 }
 sayHelloWithParams('john');
 sayHelloWithParams('john', 'smith');