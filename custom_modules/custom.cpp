/*
###############################################################################
# If you use PhysiCell in your project, please cite PhysiCell and the version #
# number, such as below:                                                      #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1].    #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# See VERSION.txt or call get_PhysiCell_version() to get the current version  #
#     x.y.z. Call display_citations() to get detailed information on all cite-#
#     able software used in your PhysiCell application.                       #
#                                                                             #
# Because PhysiCell extensively uses BioFVM, we suggest you also cite BioFVM  #
#     as below:                                                               #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1],    #
# with BioFVM [2] to solve the transport equations.                           #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# [2] A Ghaffarizadeh, SH Friedman, and P Macklin, BioFVM: an efficient para- #
#     llelized diffusive transport solver for 3-D biological simulations,     #
#     Bioinformatics 32(8): 1256-8, 2016. DOI: 10.1093/bioinformatics/btv730  #
#                                                                             #
###############################################################################
#                                                                             #
# BSD 3-Clause License (see https://opensource.org/licenses/BSD-3-Clause)     #
#                                                                             #
# Copyright (c) 2015-2018, Paul Macklin and the PhysiCell Project             #
# All rights reserved.                                                        #
#                                                                             #
# Redistribution and use in source and binary forms, with or without          #
# modification, are permitted provided that the following conditions are met: #
#                                                                             #
# 1. Redistributions of source code must retain the above copyright notice,   #
# this list of conditions and the following disclaimer.                       #
#                                                                             #
# 2. Redistributions in binary form must reproduce the above copyright        #
# notice, this list of conditions and the following disclaimer in the         #
# documentation and/or other materials provided with the distribution.        #
#                                                                             #
# 3. Neither the name of the copyright holder nor the names of its            #
# contributors may be used to endorse or promote products derived from this   #
# software without specific prior written permission.                         #
#                                                                             #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE   #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE  #
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE   #
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         #
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF        #
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS    #
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN     #
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)     #
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE  #
# POSSIBILITY OF SUCH DAMAGE.                                                 #
#                                                                             #
###############################################################################
*/

#include "./custom.h"

// declare cell definitions here 

Cell_Definition A_cell; 
Cell_Definition B_cell; 

void create_cell_types( void )
{
	// use the same random seed so that future experiments have the 
	// same initial histogram of oncoprotein, even if threading means 
	// that future division and other events are still not identical 
	// for all runs 
	
	SeedRandom( parameters.ints("random_seed") ); // or specify a seed here 
	
	// housekeeping 
	
	initialize_default_cell_definition();
	cell_defaults.phenotype.secretion.sync_to_microenvironment( &microenvironment ); 
	
	// Name the default cell type 
	
	cell_defaults.type = -1; 
	cell_defaults.name = "default"; 
	
	// set default cell cycle model 
	cell_defaults.functions.cycle_model = live; 
	
	// set default_cell_functions; 
	//cell_defaults.functions.update_phenotype = update_cell_and_death_parameters_O2_based; 
	
	// needed for a 2-D simulation: 
	
	/* grab code from heterogeneity */ 
	cell_defaults.functions.set_orientation = up_orientation; 
	cell_defaults.phenotype.geometry.polarity = 1.0;
	cell_defaults.phenotype.motility.restrict_to_2D = true; 
	
	// make sure the defaults are self-consistent. 
	cell_defaults.phenotype.secretion.sync_to_microenvironment( &microenvironment );
	cell_defaults.phenotype.sync_to_functions( cell_defaults.functions ); 

	// set the rate terms in the default phenotype 

	// first find index for a few key variables. 
	int apoptosis_model_index = cell_defaults.phenotype.death.find_death_model_index( "Apoptosis" );
	int necrosis_model_index = cell_defaults.phenotype.death.find_death_model_index( "Necrosis" );
	int nCycle_start = live.find_phase_index( PhysiCell_constants::live );
	int nCycle_end = live.find_phase_index( PhysiCell_constants::live );

	// initially no necrosis 
	cell_defaults.phenotype.death.rates[necrosis_model_index] = 0.0; 
	// cell_defaults.phenotype.death.rates[apoptosis_model_index] = 0.0;

	// set oxygen uptake / secretion parameters for the default cell type 
	//cell_defaults.phenotype.secretion.uptake_rates[oxygen_substrate_index] = 10; 
	//cell_defaults.phenotype.secretion.secretion_rates[oxygen_substrate_index] = 0; 
	//cell_defaults.phenotype.secretion.saturation_densities[oxygen_substrate_index] = 38; 
	
	// add custom data here, if any 
	

	/*** Type A ***/ 
	
	A_cell = cell_defaults; 
	A_cell.type = 0; 
	A_cell.name = "A Type Cell"; 

	// make sure the new cell type has its own reference phenotype
	A_cell.parameters.pReference_live_phenotype = &( A_cell.phenotype ); 
	
	// enable random motility 
	A_cell.phenotype.motility.is_motile = true; 
	A_cell.phenotype.motility.persistence_time = parameters.doubles( "a_cell_persistence_time" ); 
	A_cell.phenotype.motility.migration_speed = parameters.doubles( "a_cell_migration_speed" ); 
	A_cell.phenotype.motility.migration_bias = parameters.doubles( "a_cell_migration_bias" );
	
	// Set cell-cell adhesion to 5% of other cells 
	//A_cell.phenotype.mechanics.cell_cell_adhesion_strength *= parameters.doubles( "motile_cell_relative_adhesion" ); // 0.05; 
	
	// Phenotype update
	A_cell.functions.update_phenotype =  alpha_and_beta_based_proliferation; //NULL; 

	// Set proliferation and death rates
	A_cell.phenotype.cycle.data.transition_rate(0,0) = parameters.doubles("a_cell_divide_time"); // 1/mean time to cycle
	A_cell.phenotype.death.rates[apoptosis_model_index] = parameters.doubles( "a_cell_apoptosis_rate" );
	
	// Secret and uptake rates
	// Change secretion/uptake
	A_cell.phenotype.secretion.uptake_rates[0] = parameters.doubles("a_cell_alpha_uptake_rate"); 
	A_cell.phenotype.secretion.secretion_rates[0] = parameters.doubles("a_cell_alpha_secretion_rate"); 
	A_cell.phenotype.secretion.saturation_densities[0] = parameters.doubles("a_cell_alpha_saturation_density"); 
	A_cell.phenotype.secretion.uptake_rates[1] = parameters.doubles("a_cell_beta_uptake_rate"); 
	A_cell.phenotype.secretion.secretion_rates[1] = parameters.doubles("a_cell_beta_secretion_rate"); 
	A_cell.phenotype.secretion.saturation_densities[1] = parameters.doubles("a_cell_beta_saturation_density"); 

	/*** B Type Cells ***/

	B_cell = cell_defaults; 
	B_cell.type = 1; 
	B_cell.name = "B Type Cell"; 

	// make sure the new cell type has its own reference phenotype
	B_cell.parameters.pReference_live_phenotype = &( B_cell.phenotype ); 
	
	// enable random motility 
	B_cell.phenotype.motility.is_motile = true; 
	B_cell.phenotype.motility.persistence_time = parameters.doubles( "b_cell_persistence_time" ); 
	B_cell.phenotype.motility.migration_speed = parameters.doubles( "b_cell_migration_speed" ); 
	B_cell.phenotype.motility.migration_bias = parameters.doubles( "b_cell_migration_bias" );
	
	// Set cell-cell adhesion to 5% of other cells 
	//A_cell.phenotype.mechanics.cell_cell_adhesion_strength *= parameters.doubles( "motile_cell_relative_adhesion" ); // 0.05; 
	
	// Phenotype update
	B_cell.functions.update_phenotype = alpha_and_beta_based_proliferation; //NULL; 

	// Set proliferation and death rates
	B_cell.phenotype.cycle.data.transition_rate(0,0) = parameters.doubles("b_cell_divide_time"); // 1/mean time to cycle
	B_cell.phenotype.death.rates[apoptosis_model_index] = parameters.doubles( "b_cell_apoptosis_rate" ); 
	
	// Secret and uptake rates
	// Change secretion/uptake
	B_cell.phenotype.secretion.uptake_rates[0] = parameters.doubles("b_cell_alpha_uptake_rate"); 
	B_cell.phenotype.secretion.secretion_rates[0] = parameters.doubles("b_cell_alpha_secretion_rate"); 
	B_cell.phenotype.secretion.saturation_densities[0] = parameters.doubles("b_cell_alpha_saturation_density"); 
	B_cell.phenotype.secretion.uptake_rates[1] = parameters.doubles("b_cell_beta_uptake_rate"); 
	B_cell.phenotype.secretion.secretion_rates[1] = parameters.doubles("b_cell_beta_secretion_rate"); 
	B_cell.phenotype.secretion.saturation_densities[1] = parameters.doubles("b_cell_beta_saturation_density"); 

	return; 
}

void setup_microenvironment( void )
{
	// set domain parameters 
	
	// make sure to override and go back to 2D 
	if( default_microenvironment_options.simulate_2D == false )
	{
		std::cout << "Warning: overriding XML config option and setting to 2D!" << std::endl; 
		default_microenvironment_options.simulate_2D = true; 
	}

	default_microenvironment_options.use_oxygen_as_first_field= false;

	microenvironment.set_density(0, "alpha", "dimensionless");
	microenvironment.diffusion_coefficients[0] = parameters.doubles("alpha_diffusion_coefficient");
	microenvironment.decay_rates[0] = 1 / parameters.doubles("alpha_decay_rate");
	microenvironment.add_density("beta", "dimensionless");
	microenvironment.diffusion_coefficients[microenvironment.find_density_index("beta")] = parameters.doubles("beta_diffusion_coefficient");
	microenvironment.decay_rates[microenvironment.find_density_index("beta")] = 1 / parameters.doubles("beta_decay_rate");
	
	// no gradients need for this example 
	default_microenvironment_options.calculate_gradients = false; 
	
	// set Dirichlet conditions 
	default_microenvironment_options.outer_Dirichlet_conditions = false;
	
	
	std::vector<double> bc_vector = {0, 0}; // Initial values of alpha and beta
	default_microenvironment_options.Dirichlet_condition_vector = bc_vector;

	std::vector<bool> bc_activation_vector( 2, false ); 
	default_microenvironment_options.Dirichlet_activation_vector= bc_activation_vector;
	
	// initialize BioFVM 
	initialize_microenvironment(); 	
	
	return; 
}

void setup_tissue( void )
{
	Cell* pC;	
	std::vector<double> position = {0,0,0}; 

	for(int i=0; i<parameters.doubles("a_number_of_cells"); i++) {		
		position[0] = parameters.doubles("cell_x_min") + UniformRandom()*( abs(parameters.doubles("cell_x_min"))+abs(parameters.doubles("cell_x_max")));
		
		position[1] = parameters.doubles("cell_y_min") + UniformRandom()*( abs(parameters.doubles("cell_y_min"))+abs(parameters.doubles("cell_y_max")));

		pC = create_cell(A_cell); 
		pC->assign_position( position ); 
	}

	for(int i=0; i<parameters.doubles("b_number_of_cells"); i++) {		
		position[0] = parameters.doubles("cell_x_min") + UniformRandom()*( abs(parameters.doubles("cell_x_min"))+abs(parameters.doubles("cell_x_max")));
		
		position[1] = parameters.doubles("cell_y_min") + UniformRandom()*( abs(parameters.doubles("cell_y_min"))+abs(parameters.doubles("cell_y_max")));

		pC = create_cell(B_cell); 
		pC->assign_position( position ); 
	}
	
	return; 
}

std::vector<std::string> my_coloring_function( Cell* pCell ) // A-alpha cells are blue and B-beta cells are yellow. Alpha cells are the inhibitors. 
{
	std::vector<std::string> output {"", "", "", ""};
	if(pCell->type == 0) {
		if(pCell->phenotype.death.dead) {
			output[0] = "black";
			output[2] = "black";
		}
		else {
			output[0] = "blue"; 
			output[2] = "blue";
		}
	}
	else if(pCell->type == 1) {
		if(pCell->phenotype.death.dead) {
			output[0] = "brown";
			output[2] = "brown";
		}
		else {
			output[0] = "yellow";
			output[2] = "yellow";
		}
	}
	else {
		output[0] = "red";
		output[2] = "red";
	}

	
	return output; 
}

void alpha_and_beta_based_proliferation (Cell* pCell, Phenotype& phenotype, double dt)
{

	static int apoptosis_model_index = cell_defaults.phenotype.death.find_death_model_index( "Apoptosis" );
	// static int necrosis_model_index = cell_defaults.phenotype.death.find_death_model_index( "Necrosis" );

	// std::cout<<"current_phase_index = "<<phenotype.cycle.data.transition_rate(0,0) <<std::endl<<std::endl;
	// std::cout<<"Apo = "<<phenotype.death.rates[apoptosis_model_index]<<std::endl<<std::endl;
	// std::cout<<"Nec = "<<phenotype.death.rates[necrosis_model_index]<<std::endl<<std::endl;
	// std::cout<<"Volume = "<<phenotype.volume.total <<std::endl<<std::endl;
	// std::cout<<"Is motile "<<phenotype.motility.is_motile <<std::endl<<std::endl;
	// std::cout<<"Speed ="<<phenotype.motility.migration_speed <<std::endl<<std::endl;
	// std::cout<<phenotype.cycle. <<std::endl;

	static int alpha_subsubstrate_index = microenvironment.find_density_index("alpha");
	static int beta_subsubstrate_index = microenvironment.find_density_index("beta");
	// static int apoptosis_model_index = cell_defaults.phenotype.death.find_death_model_index( "Apoptosis" );
    
    double alpha_conc = pCell->nearest_density_vector()[alpha_subsubstrate_index];

	if(pCell->type == 1)
	{
		phenotype.death.rates[apoptosis_model_index] = alpha_conc * parameters.doubles("b_cell_motility_scale") * parameters.doubles("b_cell_apoptosis_scale");

		// Motility speed changing
		//phenotype.motility.migration_speed = alpha_conc * parameters.doubles("b_cell_motility_scale");
		phenotype.motility.migration_speed = 0.5 * (alpha_conc / (1-alpha_conc));
		//phenotype.motility.migration_speed = 1 / ( 1 + exp(-1 * (alpha_conc - .5)));
	}

	if(pCell->type == 0) {
		// Motility speed changing
		//phenotype.motility.migration_speed = parameters.doubles("a_cell_motility_scale") / (alpha_conc + 1e-9);
		phenotype.motility.migration_speed = 0.5 - 0.5*(alpha_conc / (1-alpha_conc));
	}





	return;
}
