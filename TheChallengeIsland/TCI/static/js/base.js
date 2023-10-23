document.addEventListener('DOMContentLoaded', function() {
    const nav_input = document.getElementById('nav-input');
    const nav_span = document.getElementById('nav-span');
    const aux = nav_input.parentElement;

    if (nav_input) {
        // Función para aplicar cambios
        const applyChanges = function() {
            aux.style.border = '3px solid greenyellow';
            nav_input.style.borderBottom = '3px solid greenyellow';
            nav_span.style.color = 'greenyellow';
        };

        // Función para restablecer cambios
        const resetChanges = function() {
            if (!nav_input.matches(':focus')) {
                aux.style.border = '3px solid rgb(172, 255, 47, 0.574)';
                if (nav_input.value.trim() === '') {
                    nav_span.style.color = 'rgb(172, 255, 47, 0.574)';
                    nav_input.style.borderBottom = '3px solid rgb(172, 255, 47, 0.574)';
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
                nav_span.style.color = 'greenyellow';
                nav_input.style.borderBottom = '3px solid greenyellow';
            } else {
                nav_input.style.borderBottom = '3px solid greenyellow';
            }
        });

        // Evento de pérdida de enfoque en el input
        nav_input.addEventListener('blur', function() {
            if (nav_input.value.trim() === '') {
                nav_span.style.color = 'rgb(172, 255, 47, 0.574)';
                nav_input.style.borderBottom = '3px solid rgb(172, 255, 47, 0.574)';
            }
        });
    }
});
