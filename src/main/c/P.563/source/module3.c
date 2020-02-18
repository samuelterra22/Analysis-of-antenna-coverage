/********************************************************************
ITU-T Draft Recommendation P.563
Version 1.0 - 23 March 2004
Version 1.1 - 04 October 2005

NOTICE

The Single Ended Assessment Model P.563 algorithm and the copyright therein
is the joint property of Psytechnics Limited, OPTICOM GmbH and SwissQual AG
and is protected by UK, US and other patents, either applied for or
registered.
Permission is granted to use this source code solely for the purpose of
evaluation of ITU-T recommendation P.563.
Any other use of this software requires a licence, which may be obtained
from:

OPTICOM GmbH 
Naegelsbachstrasse 38, D- 91052 Erlangen, Germany 
Phone: +49 9131 53 020 0		Fax: +49 9131 53 020 20  
E-mail: info@opticom.de         www.3sqm.com  


Psytechnics Limited
Fraser House, 23 Museum Street, Ipswich, IP1 1HN, UK
Phone: +44 1 473 261 800  Fax: +44 1 473 261 880
E-mail: info@psytechnics.com    www.psytechnics.com

SwissQual AG
Gewerbestrasse 2 CH-4528 Zuchwil, Switzerland
Phone: +41 32 685 08 30   Fax: +41 32 685 08 31
E-mail: sales@swissqual.com     www.swissqual.com

Psytechnics, SwissQual or Opticom can provide licences and further
information.

Authors:
      Ludovic Malfait ludovic.malfait@psytechnics.com
      Roland Bitto rb@opticom.de
      Pero Juric pero.juric@swissqual.com

********************************************************************/

#include <stdio.h>
#include <stdlib.h>

#include "defines.h"
#include "hosm.h"



/********************* 
* 
* FUNCTION: Module3
* 
* DESCRIPTION: 
*	A main function for speech statistics analysis, segmental signal-to-noise ratio 
*	and speech interruptions.
*
*	Segmental signal-to-noise ratio is calculated by analysing the range 
*	of the levels in the spectral domain for active speech frames.
*   The parameters used for speech statistics are mainly based on high order 
*	statistical evaluation of cepstral and LPC analyses. 
*	
*	Following list of parameters is calculated in this function:
*	- fCepADev
*	- fCepSkew
*	- fCepCurt
*	- fLPCCurt
*	- fLPCSkew
*	- fEstSegSNR
*	- fLPCSkewAbs
*	- fEstBGNoise
*	- fSpecLevelDev
*	- fRelNoiseFloor
*	- fSpecLevelRange
*	- fSpeechInterruptions
* 
***********************/ 

INT32 Module3(INT16 *speech_samples, const UINT32 file_length, INT32 *hosm_Nparams, 
			  FLOAT *hosm_params, FLOAT SubjectiveMOS)
{		
	typInputParameter InParameter;   
	typChannel	channel;             
	INT32		RetVal=0;              
	FLOAT       *ReferenceData=NULL;
	FLOAT       fHOSM_params[NR_OF_RESULTS];

	SubjectiveMOS = 0;
	ReferenceData = (FLOAT *)calloc(file_length, sizeof(FLOAT));
	if(ReferenceData == 0)
		return -1;

	channel.file[REFER_FILE].Fptr = 0;
	InParameter.MOS = MAX_MOS_VALUE;                                    
	                                                          
	vfloat(speech_samples, 1,ReferenceData, 1, file_length);  
	InParameter.ReferData = ReferenceData;                    
	                                                          
	InParameter.Frequency     = 8;                            
	channel.file[REFER_FILE].filetype = 3;                    
	                                                          
	RetVal = initStructures(&InParameter, &channel);          

	channel.file[REFER_FILE].FileSize = file_length*2;
	channel.file[REFER_FILE].start = 0;
	channel.file[REFER_FILE].stop  = channel.file[REFER_FILE].FileSize;
	
	RetVal = hosm (&InParameter, &channel, fHOSM_params);    

	vmov(fHOSM_params, 1, hosm_params, 1, NR_OF_RESULTS);

	*hosm_Nparams = (INT32) NR_OF_RESULTS;

	free(ReferenceData);
	
	return RetVal;
}



/********************* 
* 
* FUNCTION: module3
* 
* DESCRIPTION: 
*	A routine called by a Module3 function. It copies only 
*   the results of Module3 into tResults structure.
*
***********************/ 

void module3(INT16 *psRawSpeech, const UINT32 ulRawSpeechSz, p563Results_struct *tResults)
{
	FLOAT hosm_params[NR_OF_RESULTS];
	INT32 hosm_Nparams;

	Module3(psRawSpeech, ulRawSpeechSz, &hosm_Nparams, hosm_params, 0);

    tResults->tUnnatural.fCepADev=hosm_params[0];
    tResults->tUnnatural.fCepSkew=hosm_params[1];
	tResults->tUnnatural.fCepCurt=hosm_params[2];
	tResults->tUnnatural.fLPCCurt=hosm_params[3];
	tResults->tUnnatural.fLPCSkew=hosm_params[4];
	tResults->tUnnatural.fLPCSkewAbs=hosm_params[5];
	tResults->tMutes.fSpeechInterruptions=hosm_params[6];


	tResults->tNoise.fEstBGNoise=hosm_params[7];   
	tResults->tNoise.fEstSegSNR=hosm_params[8];
	tResults->tNoise.fRelNoiseFloor=hosm_params[9];
	tResults->tNoise.fSpecLevelDev=hosm_params[10];
	tResults->tNoise.fSpecLevelRange=hosm_params[11];

}

