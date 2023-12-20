/* search.js*/
function openwordPopup()
{
    document.querySelector('.search input[type="image"]').addEventListener('click', function (e) {
        e.preventDefault();
        var word = document.querySelector('.search input[type="text"]').value;
        fetch(`/search_word?word=${word}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('wordInfo').innerHTML = `<h2>${data.word}</h2><p>${data.meaning}</p>`;
                var button = document.getElementById('myButton');
                if (data.show_button)
                {
                    if (!button)
                    {
                        button = document.createElement('button');
                        button.id = 'myButton';
                        button.innerText = 'add to my vocab';
                        document.body.appendChild(button);
                    }
                    button.style.display = 'block';
                }
                else
                {
                    if (button)
                    {
                        button.style.display = 'none';
                    }    
                }
                var popup = document.getElementById("wordPopup");
                popup.style.visibility = "visible";
                popup.style.opacity = "1";
    
            });
    });
    }

    function closewordPopup()
    {
        var popup = document.getElementById("wordPopup");
        popup.style.visibility = "hidden";
        popup.style.opacity = "0";
    }