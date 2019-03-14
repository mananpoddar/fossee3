
        var inputDocument = document.getElementById('inputDocument');
        var fileList = [];
        
        inputDocument.addEventListener('change',function(e){
            for(var i =0;i<inputDocument.files.length;i++){
                fileList.push(inputDocument.files[i]);
                console.log('is it adsadfding Document');
            }
        })
      
        var fileCatcher = document.getElementById('file-catcher')
        fileCatcher.addEventListener('submit',function(e){
            e.preventDefault();
            fileList.forEach(function(file){
                
                sendFile(file);
                console.log("sendasdfing the files");
            });
           //after sending all the files making a get request to viewDocument 
           window.location.href="/fossee3/viewDocument";

        });
        
        sendFile = function(file){
           
            var title       =   document.getElementById('title').value
            var description =   document.getElementById('description').value
        
            var formData = new FormData();
            formData.append("Document",file)
            formData.append("title",title)
            formData.append("description",description)


          
            jQuery.ajax({
                url: "",
                type: "POST",
                data:formData,
                processData: false,
                contentType: false,
                success:function(){
                    console.log("done successfully");
                }
            });
        };