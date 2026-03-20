from flask import redirect, render_template, abort, url_for
from . import bp
from ...models import Ticket
from ... import models

@bp.get("/")
def lista():
    tickets = Ticket.query.limit(50).all()
    return render_template("tickets/lista.html", tickets=tickets)

@bp.get("/<int:ticket_id>")
def detalhe(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        abort(404)
    return render_template(
        "tickets/detalhe.html",
        ticket=ticket,
        updates=ticket.updates
    )

@bp.post("/<int:ticket_id>/close")
def fechar(ticket_id):
    models.update_ticket_status(ticket_id, "closed")
    return redirect(url_for("tickets.detalhe", ticket_id=ticket_id))

@bp.post("/<int:ticket_id>/reopen")
def reabrir(ticket_id):
    models.update_ticket_status(ticket_id, "open")
    return redirect(url_for("tickets.detalhe", ticket_id=ticket_id))


