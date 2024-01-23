update_vendor_assets:
	# Note: call this command from the same folder your Makefile is located
	# Note: this run only update minor versions.
	# Update major versions manually, you can use "ncu" for this.
	# https://nodejs.dev/en/learn/update-all-the-nodejs-dependencies-to-their-latest-version/#update-all-packages-to-the-latest-version

	# Update
	npm update

	# Bootstrap https://github.com/twbs/bootstrap
	rm -r sedos_dashboard/static/vendors/bootstrap/scss/*
	cp -r node_modules/bootstrap/scss/* sedos_dashboard/static/vendors/bootstrap/scss/
	rm -r sedos_dashboard/static/vendors/bootstrap/js/*
	cp node_modules/bootstrap/dist/js/bootstrap.min.js* sedos_dashboard/static/vendors/bootstrap/js/

	# Bootstrap-Select https://github.com/snapappointments/bootstrap-select
#	rm -r sedos_dashboard/static/vendors/bootstrap-select/css/*
#	cp -r node_modules/bootstrap-select/dist/css/* sedos_dashboard/static/vendors/bootstrap-select/css/
#	rm -r sedos_dashboard/static/vendors/bootstrap-select/js/*
#	cp node_modules/bootstrap-select/dist/js/bootstrap-select.js sedos_dashboard/static/vendors/bootstrap-select/js/

	# jQuery https://github.com/jquery/jquery
#	rm -r sedos_dashboard/static/vendors/jquery/js/*
#	cp node_modules/jquery/dist/jquery.min.* sedos_dashboard/static/vendors/jquery/js/

	# Done
