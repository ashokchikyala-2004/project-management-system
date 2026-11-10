fetch('/api/projects/')
    .then(response => response.json())
    .then(data => {
        let output = "";

        data.forEach(project => {
            output += `
                <div class="card">
                    <h3>${project.name}</h3>
                    <p>${project.description}</p>
                </div>
            `;
        });

        document.getElementById("project-list").innerHTML = output;
    })
    .catch(error => console.log(error));