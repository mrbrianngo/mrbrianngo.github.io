document.addEventListener('DOMContentLoaded', function(){
  var form = document.getElementById('email-form');
  var email = document.getElementById('email');
  var msg = document.getElementById('form-message');

  form.addEventListener('submit', function(e){
    e.preventDefault();
    var val = email.value.trim();
    if(!val){
      msg.textContent = 'Please enter your email.';
      msg.style.color = '#b91c1c';
      email.focus();
      return;
    }
    // simple email check
    var re = /^[\w.%+-]+@[\w.-]+\.[A-Za-z]{2,}$/;
    if(!re.test(val)){
      msg.textContent = 'Please enter a valid email address.';
      msg.style.color = '#b91c1c';
      email.focus();
      return;
    }

    // For now we just simulate success. Replace with an API call if/when you have a backend.
    msg.style.color = '#064e3b';
    msg.textContent = 'Thanks! We\'ll notify you when we launch.';
    form.reset();
  });
});