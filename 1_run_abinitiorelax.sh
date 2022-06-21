#!/bin/bash
#SBATCH --account=rrg-skal
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --time=12:00:00
#SBATCH --mem=0G
#SBATCH --job-name=test
#SBATCH --output=%x-%j.out
#SBATCH --mail-type=ALL,TIME_LIMIT_90
#SBATCH --mail-user=vs2chu@uwaterloo.ca
pwd; hostname; date

module load rosetta/3.12

workingdir=/home/vchu/scratch/AGGREPRO/test-2
ROSETTA3=/cvmfs/soft.computecanada.ca/easybuild/software/2020/avx2/MPI/intel2020/openmpi4/rosetta/3.12

# Generate options file
fragment_fasta="P09651_Count1_Posn289-329.fasta"
frag3="aat000_03_05.200_v1_3"
frag9="aat000_09_05.200_v1_3"
psipred="t000_.psipred_ss2"
nstruct="10000"

$workingdir/2_run_options.sh $ROSETTA3 $workingdir $fragment_fasta $frag3 $frag9 $psipred $nstruct
echo ">>>> AbinitioRelax options generated <<<<"

# Run AbinitioRelax
mpiexec -np 32 $ROSETTA3/bin/AbinitioRelax.mpi.linuxiccrelease @options > abinitio_log.log

# Produce score vs. rms plot
$workingdir/3_run_extractrmsd.sh $workingdir $ROSETTA3 "10000"

pwd; hostname; date
