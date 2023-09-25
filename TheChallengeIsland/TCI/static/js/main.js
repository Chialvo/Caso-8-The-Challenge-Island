const nav = document.getElementById('navbar');
var aux =this.window.innerHeight
console.log(aux)

window.addEventListener('scroll', function() 
    {     
    showNav()
    })

function showNav(){
        console.log("fuga")
        if (window.pageYOffset > (this.window.innerHeight-100)) 
        {
        nav.setAttribute("style", "background-color:#57a631;")
        console.log("agregar")
        } 
        else 
        {
        nav.setAttribute("style", "background-color: transparent; transition: all .5s;");
        console.log("quitar")
        }  
    }