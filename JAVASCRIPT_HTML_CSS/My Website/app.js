//! Add event listener to each control button
function addControlButtonEventListener(button) {
    button.addEventListener("click", () => {
      //! Remove active class from current button and add it to clicked button
      const activeButton = document.querySelector(".control.active-btn");
      activeButton.classList.remove("active-btn");
      button.classList.add("active-btn");
  
      //! Remove active class from current element and add it to corresponding element
      const activeElement = document.querySelector(".active");
      activeElement.classList.remove("active");
      const { id } = button.dataset;
      document.getElementById(id).classList.add("active");
    });
  }
  
  //! Add event listener to theme button
  function addThemeButtonEventListener() {
    const themeButton = document.querySelector(".theme-btn");
    themeButton.addEventListener("click", () => {
      document.body.classList.toggle("light-mode");
    });
  }
  
  //! Initialize event listeners
  (function init() {
    const controlButtons = document.querySelectorAll(".control");
    controlButtons.forEach(addControlButtonEventListener);
    addThemeButtonEventListener();
  })();
  