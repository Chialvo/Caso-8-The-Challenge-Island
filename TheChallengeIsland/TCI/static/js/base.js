document.addEventListener('DOMContentLoaded', function() {
    const nav_input = document.getElementById('nav-input');
    const nav_span = document.getElementById('nav-span');
    const aux = nav_input.parentElement;

    if (nav_input) {
        // Función para aplicar cambios
        const applyChanges = function() {
            aux.style.border = '3px solid #a9cd5b';
            nav_input.style.borderBottom = '3px solid #a9cd5b';
            nav_span.style.color = '#a9cd5b';
        };

        // Función para restablecer cambios
        const resetChanges = function() {
            if (!nav_input.matches(':focus')) {
                aux.style.border = '3px solid #209e60';
                if (nav_input.value.trim() === '') {
                    nav_span.style.color = '#209e60';
                    nav_input.style.borderBottom = '3px solid #209e60';
                }
            }
        };

        // Evento al entrar en el input o el span
        nav_input.addEventListener('mouseenter', applyChanges);
        nav_span.addEventListener('mouseenter', applyChanges);

        // Evento al salir del input o el span
        nav_input.addEventListener('mouseleave', resetChanges);
        nav_span.addEventListener('mouseleave', resetChanges);

        // Evento de enfoque en el input
        nav_input.addEventListener('focus', applyChanges);

        // Evento de pérdida de enfoque en el input
        nav_input.addEventListener('blur', resetChanges);

        // Evento de entrada de texto en el input
        nav_input.addEventListener('input', function() {
            if (nav_input.value.trim() === '') {
                nav_span.style.color = '#a9cd5b';
                nav_input.style.borderBottom = '3px solid #a9cd5b';
            } else {
                nav_input.style.borderBottom = '3px solid #a9cd5b';
            }
        });

        // Evento de pérdida de enfoque en el input
        nav_input.addEventListener('blur', function() {
            if (nav_input.value.trim() === '') {
                nav_span.style.color = '#209e60';
                nav_input.style.borderBottom = '3px solid #209e60';
            }
        });
    }
});
