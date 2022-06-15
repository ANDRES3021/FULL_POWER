document.addEventListener('DOMContentLoaded', () => {
    let checkboxes = document.querySelectorAll(".mycheckbox");
    
    document.addEventListener('change', function() {
        let content = [];
        checkboxes.forEach((checkbox) => {
            if (checkbox.checked) {
                content += checkbox.getAttribute('data-name') + ",";
            }
        });
        document.getElementById("text").innerText = content;
    });
 
});


    