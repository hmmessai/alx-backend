import { createQueue } from 'kue';

const queue = createQueue({name: 'push_notification_code'});

const job = queue.create('push_cotification_codde', {
  phoneNumber: '251933993399',
  message: 'Account registered',
});

job
  .on('enqueue', () => {
    console.log('Notification job create:', job.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');
  });
job.save();
