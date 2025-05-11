window.onload = function () {
    const logo = document.getElementById("logo");
    if (logo) {
        logo.addEventListener("click", () => {
            window.location.href = "/";
        });
    }
};
