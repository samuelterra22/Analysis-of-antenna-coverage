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

#ifndef PSEAM_DEFINITIONS
	#define PSEAM_DEFINITIONS

#define BUGFIX_ON
#ifdef BUGFIX_ON
#if(1)
#define BUGFIX_01 // buffer overflow: find_pos_neg_first_last(): crashes in debug mode
#define BUGFIX_05 // buffer overflow due to type conversion negative int -> unsigned int: FFT_Gaps(): crashes in debug mode
#define BUGFIX_04	// buffer overflow due to illegal value change: module1()
#define BUGFIX_06	// division by zero: VTPPeakTracker()
#define BUGFIX_07	// division by zero: smooth_averagesf()
#define BUGFIX_10	// division by zero: Tract_Averages()
#define BUGFIX_11	// division by zero: Correlations_Zero_Cross()
#endif

#if(1)
#define BUGFIX_03 // uninitialized variable: module1()
#endif

#if(1)
#define BUGFIX_02 // division by zero: find_first_only()
#endif

#if(1)
#define BUGFIX_08 // division by zero: LPC_Burg()
#endif

#if(1)
#define BUGFIX_09	// log limit: vlogz()
#endif

#endif


/*******************************
*     Constant definitions     *
*******************************/

	/* General use definitions */
	#define MIN_SIGNAL_LEN		40000		/* 5 seconds at 8kHz */
	#define MAX_SIGNAL_LEN		160000		/* 20 seconds at 8kHz */
	#define INVALID_CODE		-999
	#define SAMPLE_FREQUENCY	8000
	#define TARGET_SPEECH_LEVEL	-26

	#define PI		3.141592653589793f
	#define TWOPI	6.283185307179586f

	#define VAD_FRAME_LEN				32		/* Frame length for VAD calculation */
	#define VAD_MIN_SPEECH_SECTION_LEN	4		/* Mimimum length for speech sections */
	#define VAD_JOIN_SPEECH_SECTION_LEN	50		/* Miminum length between 2 consecutives speech sections */
	#define REF_DBOV					90.3f	/* Maximum level (dB) an INT16 signal could reach */


	#ifndef FALSE
		#define     FALSE                           0
	#endif

	#ifndef TRUE
		#define     TRUE                            1
	#endif

/*******************************
*        Type definitions      *
*******************************/

	typedef char				INT8;         
	typedef unsigned char	UINT8; 
	
	typedef short				INT16;
	typedef unsigned short	UINT16;
	typedef long				INT32;
	typedef unsigned long	UINT32;

	typedef int					INT;
	typedef unsigned int		UINT;

	typedef char bool ;


#define FLOAT_64  1
#if FLOAT_64
	typedef  double		FLOAT;
#else
	typedef  float			FLOAT;
#endif

	typedef short				BOOL;


/*******************************
*    Structure definitions     *
*******************************/

	/* Structure holding preprocessed signal and VAD output */
	typedef struct
	{
		FLOAT	*pfSignal;
		FLOAT	*pfSignal26dB;
		FLOAT	*pfSignal26dB_IRS;
		INT32	lSignalLen;
		FLOAT	fLevelNorm;
		FLOAT	*pfVadProfile;
		INT32	lVadProfileLen;
	} SignalInfo_struct;

	/* Structure storing basic speech descriptors */
	typedef struct
	{
		FLOAT	fSpeechLevel;
		FLOAT	fPitchAverage;
		FLOAT	fSpeechSectionLevelVar;
	} basic_desc_struct;

	/* Structure storing noise analysis parameters */
	typedef struct
	{

		FLOAT fEstBGNoise;
	    FLOAT fEstSegSNR;
		FLOAT fSpecLevelDev;
		FLOAT fSpecLevelRange;
		FLOAT fRelNoiseFloor;

		FLOAT	fNoiseLevel;
		FLOAT	fSnr;
		FLOAT	fHiFreqVar;
		FLOAT	fSpectralClarity;

		FLOAT fLocalBGNoise;
		FLOAT fLocalBGNoiseMean;
		FLOAT fLocalBGNoiseLog;
		FLOAT fLocalMeanDistSamp; 

		FLOAT fGlobalBGNoise;	

	} noise_analysis_struct;

	/* Structure storing mute parameters */
	typedef struct
	{
		FLOAT	fMuteLength;
		FLOAT fSpeechInterruptions;
		FLOAT fSharpDeclines;
		FLOAT fUnnaturalSilenceMean;


	} mutes_struct;

	/* Structure storing unnatural speech parameters */
	typedef struct
	{
		FLOAT fConsistentArtTracker;
		FLOAT fVtpMaxTubeSection;
		FLOAT fFinalVtpAverage;
		FLOAT fVtpPeakTracker;
		FLOAT fArtAverage;
		FLOAT fVtpVadOverlap;
		FLOAT fPitchCrossCorrelOffset;
		FLOAT fPitchCrossPower;

		FLOAT fFrameRepeats;
		FLOAT fFrameRepeatsMean;     
		FLOAT fUBeeps;	
		FLOAT fUBeepsMean;		
		FLOAT fUnBeepsMeanDistSamp;  
		FLOAT fRobotisation;

		FLOAT fCepADev;			   
		FLOAT fCepSkew;			           
		FLOAT fCepCurt;			           
		FLOAT fLPCCurt;			           
		FLOAT fLPCSkew;			           
		FLOAT fLPCSkewAbs;	

	} unnatural_struct;

	/* Structure storing speech extraction parameters */
	typedef struct
	{

		FLOAT fBasicVoiceQualityAsym;
		FLOAT fBasicVoiceQuality;

	} speech_extract_struct;

	/* Structure grouping all parameters */
	typedef struct
	{
		mutes_struct			tMutes;
		noise_analysis_struct	tNoise;
		unnatural_struct		tUnnatural;
		basic_desc_struct		tBasicDesc;
		speech_extract_struct	tSpeechExtract;

		INT32 lPartition;
		FLOAT fPredictedMos;
		FLOAT fIeValue;

	} p563Results_struct;


#endif
