// Capturando os elementos do HTML
const titulo = document.getElementById('titulo');
const listaNaoOrdenada = document.querySelector('ul');
const link = document.getElementById('link');
const listaOrdenada = document.getElementById('lista-ordenada');

// Adicionando conteúdo textual aos elementos
titulo.innerText = "Título da Página";
link.innerText = "Link para Proz Educação";

// Adicionando itens à lista não ordenada usando innerHTML
listaNaoOrdenada.innerHTML = `
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
`;

// Adicionando itens com links à lista ordenada usando innerHTML
listaOrdenada.innerHTML = `
    <li><a href="https://www.exemplo.com">Item 1</a></li>
    <li><a href="https://www.exemplo.com">Item 2</a></li>
    <li><a href="https://www.exemplo.com">Item 3</a></li>
`;
