# store standard roots in views like login/homepage/subpages etc.
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from ..models import Seat, SeatingChart
from .. import db

# Blueprint means it has a lot of urls inside here 
views_admin = Blueprint('views_admin', __name__, template_folder='templates')

@views_admin.route('/')
@login_required
def home():
    return render_template("admin_home.html", user=current_user) # here we can reference our current logged user also for template


@views_admin.route('/import-seating', methods=['GET','POST'])
@login_required
def import_seating():
        return render_template('admin_import_seating.html', user=current_user)

"""     try:
        
        chart = SeatingChart(name=request.form.get('chart_name', 'New Chart'))
        db.session.add(chart)
        # Read file content from request
        file_content = request.files['seating_file'].read().decode('utf-8')
        rows = file_content.strip().split('\n')
        
        # Process each row
        for row_idx, row in enumerate(rows[1:], 1):  # Skip header row
            columns = row.strip().split('\t')[1:]  # Skip row number column
            for col_idx, seat_type in enumerate(columns):
                col_letter = chr(65 + col_idx)  # Convert 0,1,2... to A,B,C...
                
                # Create or update seat
                seat = Seat.query.filter_by(
                    row_number=row_idx,
                    column_letter=col_letter
                ).first() or Seat()
                
                seat.row_number = row_idx
                seat.column_letter = col_letter
                seat.seat_type = seat_type
                seat.modified_by_admin_id = current_user.id
                
                db.session.add(seat)
        
        db.session.commit()
        flash('Seating chart imported successfully!', category='success')
        
    except Exception as e:
        db.session.rollback()
        flash(f'Error importing seating chart: {str(e)}', category='error')
     """
