from pathlib import Path
from flask import Flask, render_template, request
# import math
import course_search as search

app = Flask(__name__)




@app.route("/")
def home() -> str:
    """
    home page
    :return:
    """
    return render_template("home.html")


@app.route("/results", methods=["POST"])
def results() -> str:
    """
    result page
    :return:
    """
    query_text = request.form["query"]  # Get the raw user query from home page
    search.topmenu(query_text)

    ## add this to the final return statement and add a field in results.html
    ##add all of these to a string and then return a list of courses
            print("courses has", len(schedule.courses), 'elements', end="\n\n")
            print('here are the first 10')
            for course in schedule.courses[:10]:
                print_course(course)
            print('\n' * 3)
    return render_template("results.html", query=##)


# @app.route("/results/<int:page_id>/<int:total_pages>", methods=["GET", "POST"])
# def next_page(page_id: int, total_pages: int) -> str:
#     """
#     "next page" to show more results
#     :param page_id:
#     :param total_pages:
#     :return:
#     """
#     return render_template("results.html", query=##)


# @app.route("/doc_data/<doc_id>")
# def doc_data(doc_id: int) -> str:
#     """
#     document page
#     :param doc_id:
#     :return:
#     """
#     ##make a doc page for a class
#     return render_template("doc.html", here=doc_dict)


if __name__ == "__main__":
    app.run(debug=True, port=2400)