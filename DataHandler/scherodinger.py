# from schrodinger import structure
# from schrodinger import maestro
# from schrodinger.structutils import rmsd
# from schrodinger.job import job_control, job


# maestro.initialize()
# mae_file = ''
# reader = structure.StructureReader(mae_file)
# structures = list(reader)
# job_conf = job.ControlFile()
# job_conf.settings.prim_sec_structure = True  # Example setting
# job_control.run_job(job_conf, input_struct=structures)
# maestro.finalize()