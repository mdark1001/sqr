function ready(){
    console.log("Here is the js of surveies")
    const token = document.getElementsByName('csrfmiddlewaretoken')[0]; 

    // Show modal for create a survey
    const buttonCreateSurvey = document.getElementById('btnCreateSurvey')
    buttonCreateSurvey.addEventListener('click',function(e){
        let modalCreate = document.getElementById('modalCreateSurvey')
        modalCreate.classList.add('is-active');
        let rootE = e.target.closest('div.container')
        rootE.classList.add('is-clipped')
    })
    // buton that create a new survey using ajax
    const createNewSurveyButton = document.getElementById('createNewSurveyButton')
    createNewSurveyButton.addEventListener('click',function(e){
        let name = document.getElementById('newSurvey')  
        
        if(!name.value){
            name.classList.add('is-danger')
            setTimeout(()=> name.classList.remove('is-danger'))
            return;
        }
        let formData = new FormData();
        formData.append('name',name.value)
        formData.append('csrfmiddlewaretoken',token.value)
        fetch('/survey/',{
            'method': 'POST',
            body: formData
        }).then(response => response.json())
        .then(data => window.location.href='/survey/'+data.survey_id+'/edit')
    });


}

ready();