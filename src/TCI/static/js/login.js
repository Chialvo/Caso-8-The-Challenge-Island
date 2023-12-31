document.addEventListener('DOMContentLoaded', function(){
    const input_useranme = document.getElementById("input-username");
    const input_password = document.getElementById("input-password");
    const span_eye = document.getElementById("span-eye");
    const div_username = document.getElementById("div-username");
    const div_password = document.getElementById("div-password");

    if(input_useranme && input_password){

        const activarDivUsername = function(){
            div_username.style.borderBottom = '3px solid #a9cd5b';
        }

        const desactivarDivUsername = function(){
            if (!input_useranme.matches(':focus')) {
                div_username.style.borderBottom = '3px solid #209e60';
                if (input_useranme.value.trim()) {
                    div_username.style.borderBottom = '3px solid #a9cd5b';
                } 
            }
        }
        input_useranme.addEventListener('blur', function() {
            if (input_useranme.value.trim() === '') {
                div_username.style.borderBottom = '3px solid #209e60';
            }   
        });

    input_useranme.addEventListener('mouseenter', activarDivUsername);
    input_useranme.addEventListener('mouseleave', desactivarDivUsername);


    const activarDivPassword = function(){
        div_password.style.borderBottom = '3px solid #a9cd5b';
        input_password
    }

    const desactivarDivPassword = function(){
        if (!input_password.matches(':focus')) {
            div_password.style.borderBottom = '3px solid #209e60';
            if (input_password.value.trim()) {
                div_password.style.borderBottom = '3px solid #a9cd5b';
            } 
        }
    }
    input_password.addEventListener('blur', function() {
        if (input_password.value.trim() === '') {
            div_password.style.borderBottom = '3px solid #209e60';
        }
    });

    input_password.addEventListener('mouseenter', activarDivPassword);
    input_password.addEventListener('mouseleave', desactivarDivPassword);
    span_eye.addEventListener('mouseenter', activarDivPassword);
    span_eye.addEventListener('mouseleave', desactivarDivPassword);

    };
    if(span_eye){
        let passwordVisible = false;
        span_eye.addEventListener('click', () => {
            passwordVisible = !passwordVisible;
        if (passwordVisible) {
            input_password.type = 'text';
            span_eye.textContent = 'visibility';
        } else {    
            input_password.type = 'password';
            span_eye.textContent = 'visibility_off';
    }
    });
    }


});
