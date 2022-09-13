// const myModal = document.getElementById('myModal')
// const myInput = document.getElementById('myInput')

$("#myModal").click(function(){    if(confirm("정말 등록하시겠습니까 ?") == true){        alert("등록되었습니다");    }    else{        return ;    }});
