let root = document.documentElement;
let color = document.getElementById('box-color').getAttribute('data-value');
root.style.setProperty('--color-fondo', color);