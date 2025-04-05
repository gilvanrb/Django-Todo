//função que pergunta ao usuario se ele quer mesmo escluir a tarefa

document.querySelectorAll('.delete-btn').forEach(
    btn => {
        btn.addEventListener("click", function(e){
            e.preventDefault();

            const delink = this.getAttribute("href");

            if(delink && confirm("Quer deletar esta tarefa?"))
            {
                window.location.href = delink;
            }



        });
    }
);

//função para pesquisar

document.getElementById("search-bt").addEventListener("click", function(){
    document,getElementById("search-form").onsubmit();
});


