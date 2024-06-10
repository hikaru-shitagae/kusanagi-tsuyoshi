document.addEventListener('DOMContentLoaded', function(){
  const sake = document.getElementsByClassName('sake');
  for (var i = 0; i < sake.length; i++){
    const button = sake[i].querySelector('button.button');
    const mask = sake[i].querySelector('.mask');
    const modal = sake[i].querySelector('.modal');

    button.addEventListener('click', () => {
      mask.classList.remove('hidden');
      modal.classList.remove('hidden');
    });

    mask.addEventListener('click', () => {
      mask.classList.add('hidden');
      modal.classList.add('hidden');
    });
  }
})