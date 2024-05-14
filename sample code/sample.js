document.getElementById("the_chosen_one").addEventListener("load", () => {
    console.log("the chosen one is loaded");
});

function hello(persons = 1) {
    for(var i=0; i<persons; i++)
        console.log("bye");
}

//NOTE: this is an anonimous note
//NOTE(jtu): jtu left a note here
 
class DummyClass extends Object {
    constructor(a=undfined) {
        this.a = a;
    }

    print() {
        console.log("this is a:" + a);
    }
}