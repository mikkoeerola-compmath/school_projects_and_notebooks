const mongoose = require('./../mongoose');

const eventSchema = new mongoose.Schema({
    name: {
        type: String,
        validate: {
            validator: function(word) {
                return word.length <= 50 & word.length > 0
            }
        },
        required: [true, 'Name is required!']
    },
    date: {
        type: String,
        required: [true, 'Date is required!']
    },
    status: {
        type: String,
        default: 'planned',
        enum: {
            values: ['planned', 'completed', 'cancelled', 'rejected'],
            message: 'Status must be either planned, completed, cancelled, or rejected!'
        }
    },
    description: String
});

const Event = mongoose.model('Event', eventSchema);

module.exports = Event;
