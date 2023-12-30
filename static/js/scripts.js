function logout() {
    let options = {
        method: "POST"
    };
    fetch("/auth/jwt/logout", options)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            window.location.href = "/";
            return response.json();
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
}

function addMember() {
    const error_div = document.querySelector("#error_message")
    let formData = {
        surname: document.querySelector("#surname_to_add").value,
        name: document.querySelector("#name_to_add").value,
        patronymic: document.querySelector("#patronymic_to_add").value,
        birth_date: document.querySelector("#birth_date_to_add").value
    }
    let options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    };
    fetch("/admin/members/insert", options)
        .then(response => {
            if (!response.ok) {
                error_div.style.display = "block"
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            window.location.href = "/admin/members";
            return response.json();
        })
        .then(data => {
            console.log(data)
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
}

function updateMember(mem_id) {
    const error_div = document.querySelector("#error_message")
    error_div.style.display = "none";
    let formData = {
        id: mem_id,
        surname: document.querySelector("#_" + mem_id.toString() + "_1").value,
        name: document.querySelector("#_" + mem_id.toString() + "_2").value,
        patronymic: document.querySelector("#_" + mem_id.toString() + "_3").value,
        birth_date: document.querySelector("#_" + mem_id.toString() + "_4").value
    }
    console.log(formData)
    let options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    };
    fetch("/admin/members/update", options)
        .then(response => {
            if (!response.ok) {
                error_div.style.display = "block"
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            window.location.href = "/admin/members";
            return response.json();
        })
        .then(data => {
            console.log(data)
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
}


function deleteMember(mem_id) {
    let formData = {
        id: mem_id
    }
    let options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    };
    // Отправка fetch-запроса
    fetch("/admin/members/delete", options)
        .then(response => {
            if (!response.ok) {
                error_div.style.display = "block"
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            window.location.href = "/admin/members";
            return response.json();
        })
        .then(data => {
            console.log(data)
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
}

function reg() {
    const error_div = document.querySelector("#error_message")
    let formData = {
        email: document.querySelector("#email").value,
        password: document.querySelector("#password").value,
        is_active: true,
        is_superuser: false,
        is_verified: false
    };
    let options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    };
    console.log(formData);
    // Отправка fetch-запроса
    fetch("/auth/register", options)
        .then(response => {
            if (!response.ok) {
                if (response.status === 400) {
                    throw new Error("Bad Request");
                } else {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            if (!data.error) {
                window.location.href = "./";
            }
        })
        .catch(error => {
            console.error('Fetch error:', error);
            if (error.message === "Bad Request") {
                error_div.style.display = "block";
            }
        });
}

function reg() {
    const error_div = document.querySelector("#error_message")
    error_div.style.display = "none";
    let formData = new FormData();
    formData.append('username', document.querySelector("#email").value);
    formData.append('password', document.querySelector("#password").value);

    let options = {
        method: "POST",
        body: formData
    };
    fetch("/auth/jwt/login", options)
        .then(response => {
            if (!response.ok) {
                if (response.status === 400) {
                    throw new Error("Bad Request");
                } else {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
            }
            window.location.href = "admin/members";
            return response.json();
        })
        .then(data => {
            console.log(data)
        })
        .catch(error => {
            console.error('Fetch error:', error);

            if (error.message === "Bad Request") {
                error_div.style.display = "block";
            }
        });
}
