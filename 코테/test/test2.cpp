#include <stdio.h>

typedef enum
{
    MEM_LI_ERM_PRAMC_0 = 0,     /* RAM Controller */
    MEM_LI_ERM_PRAMC_1,         /* RAM Controller */
    MEM_LI_ERM_EDMA_A_TCD,
    MEM_LI_ERM_EDMA_B_TCD,
    MEM_LI_ERM_FEC_MIB1,
    MEM_LI_ERM_FEC_RIF1,
    MEM_LI_ERM_PFLASH_PORT_0,   /* PFLASH */
    MEM_LI_ERM_PFLASH_PORT_1,   /* PFLASH */
    MEM_LI_ERM_AIPS_0,
    MEM_LI_ERM_AIPS_1,
    MEM_LI_ERM_FEC_E2EECC,
    MEM_LI_ERM_CSE,
    MEM_LI_ERM_SIPI,
    MEM_LI_ERM_CORE0_INSTRUCTION,
    MEM_LI_ERM_CORE0_DATA,
    MEM_LI_ERM_CORE1_INSTRUCTION,
    MEM_LI_ERM_CORE1_DATA,
    MEM_LI_ERM_EDMA_A_E2EECC,
    MEM_LI_ERM_EDMA_B_E2EECC,
    MEM_LI_ERM_EBI_E2EECC,
    MEM_LI_ERM_MAX_ERM_CHANNEL
} MEM_LI_MCAL_ERM_CHANNEL;

typedef enum
{
	ERM_INIT,
    ERM_PRAMC_0,     /* RAM Controller */
    ERM_PRAMC_1,         /* RAM Controller */
    ERM_EDMA_A_TCD,
    ERM_EDMA_B_TCD,
    ERM_FEC_MIB1,
    ERM_FEC_RIF1,
    ERM_PFLASH_PORT_0,   /* PFLASH */
    ERM_PFLASH_PORT_1,   /* PFLASH */
    ERM_AIPS_0,
    ERM_AIPS_1,
    ERM_FEC_E2EECC,
    ERM_CSE,
    ERM_SIPI,
    ERM_CORE0_INSTRUCTION,
    ERM_CORE0_DATA,
    ERM_CORE1_INSTRUCTION,
    ERM_CORE1_DATA,
    ERM_EDMA_A_E2EECC,
    ERM_EDMA_B_E2EECC,
    ERM_EBI_E2EECC,
    ERM_CHANNEL_INVALID
} MCAL_ERM_CHANNEL;

// void myfunc(MCAL_ERM_CHANNEL n){
// 	if(n == )
// }
int main(void){
	int test;
	char * test2;
	test = (MCAL_ERM_CHANNEL)MEM_LI_ERM_EDMA_B_TCD;
	// test2 = (MCAL_ERM_CHANNEL)MEM_LI_ERM_EDMA_B_TCD;
	// printf("%s ", (MCAL_ERM_CHANNEL)MEM_LI_ERM_PRAMC_0);
	// printf("%d ", (MCAL_ERM_CHANNEL)MEM_LI_ERM_EDMA_B_TCD);

	// printf("%s", test2);

	if(test == ERM_EDMA_A_TCD)printf("1");
	else printf("2");
	return 0;
}



int arr	[8] = 0;
arr[10] = 1;