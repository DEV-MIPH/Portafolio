import { Injectable } from '@angular/core';
import { Configuration, EmailsApi, EmailTransactionalMessageData ,TemplatesApi } from '@elasticemail/elasticemail-client-ts-axios';


@Injectable({
  providedIn: 'root'
})
export class ElasticMailService {

  constructor() { }
  
  config = new Configuration({
    apiKey: "A9A1BBE6357DF3A3A147128ECD410D0FD78B4BB7A0DE2ECDEA5F9675E64A60016006F7E76F1AE82A3503947D0B808E3C"
  });

  emailsApi = new EmailsApi(this.config);

  templatesApi = new TemplatesApi(this.config);
  
  templateName = "Plantilla 1";

  loadTemplate = async (): Promise<any | undefined> => {
    try{
      const response = await this.templatesApi.templatesByNameGet(this.templateName);
      console.log('API called successfully.');
      const templateBody = response.data.Body;
      console.log(templateBody);
      return templateBody;
    }catch(error){
      console.log("error");
      return undefined;

    }
  } 

   sendEmail = async (correo:any): Promise<void> => {

    
    const body = await this.loadTemplate();
    console.log(body[0]);
    console.log(body[0].ContentType);
    console.log(body[0].Charset);
    console.log(body[0].Content);
    
      

    const emailTransactionalMessageData:EmailTransactionalMessageData = {
      Recipients: { 
        To: [correo] 
      },
      Content: {
        Body: [{
          ContentType: body[0].ContentType,
          Charset: body[0].Charset,
          Content: body[0].Content
        }],
        From: "micocinillaapp@outlook.com",
        Subject: "Gracias por usar Mi CocinillaAPP"
      }
    };
    this.emailsApi.emailsTransactionalPost(emailTransactionalMessageData).then((response) => {
      console.log('API called successfully.');
      console.log(response.data);
    }).catch((error) => {
      console.error(error);
    });

  }
  
  
    
  

}
